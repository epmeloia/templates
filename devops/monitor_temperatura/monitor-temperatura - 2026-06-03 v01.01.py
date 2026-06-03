# ------------------------------------------
# monitor-temperatura.py
# ------------------------------------------
# Desenvolvimento através do CHARTGPT\CODEX
# ------------------------------------------
# Alteração:
#
# - 2026-06-03 v01.00
# - Falta adequar o arquivo requirements.txt
#
# - 2026-06-03 v01.01
# - Atualizado o arquivo requirements.txt
#   pywin32==311
# - Executado o comando de Instalação direta
#   cd "D:\_DEVOPS\Monitor_Temperatura"; py -3 -m pip install wmi==1.5.1 pywin32==311
# - 
#
# -----------------------------------
#

import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from datetime import datetime


UPDATE_INTERVAL_MS = 2000


@dataclass
class TemperatureReading:
    value_celsius: float | None
    source: str
    message: str = ""


class CpuTemperatureProvider:
    """Busca a temperatura da CPU usando fontes WMI comuns no Windows."""

    def __init__(self) -> None:
        self._wmi = None

        try:
            import wmi

            self._wmi = wmi
        except ImportError:
            self._wmi = None

    def read_cpu_temperature(self) -> TemperatureReading:
        if self._wmi is None:
            return TemperatureReading(
                None,
                "Dependencia ausente",
                "Instale as dependencias com: pip install -r requirements.txt",
            )

        reading = self._read_hardware_monitor()
        if reading.value_celsius is not None:
            return reading

        reading = self._read_acpi_thermal_zone()
        if reading.value_celsius is not None:
            return reading

        return TemperatureReading(
            None,
            "Indisponivel",
            "Nenhum sensor de CPU foi encontrado pelo Windows.",
        )

    def _read_hardware_monitor(self) -> TemperatureReading:
        for namespace in ("root\\LibreHardwareMonitor", "root\\OpenHardwareMonitor"):
            try:
                connection = self._wmi.WMI(namespace=namespace)
                sensors = connection.Sensor()
            except Exception:
                continue

            cpu_temperatures = [
                sensor.Value
                for sensor in sensors
                if getattr(sensor, "SensorType", "") == "Temperature"
                and "cpu" in getattr(sensor, "Name", "").lower()
            ]

            if cpu_temperatures:
                return TemperatureReading(
                    round(max(cpu_temperatures), 1),
                    namespace,
                )

        return TemperatureReading(None, "Hardware monitor")

    def _read_acpi_thermal_zone(self) -> TemperatureReading:
        try:
            connection = self._wmi.WMI(namespace="root\\wmi")
            zones = connection.MSAcpi_ThermalZoneTemperature()
        except Exception:
            return TemperatureReading(None, "ACPI")

        temperatures = []
        for zone in zones:
            raw_value = getattr(zone, "CurrentTemperature", None)
            if raw_value:
                celsius = (raw_value / 10.0) - 273.15
                if -20 <= celsius <= 130:
                    temperatures.append(celsius)

        if temperatures:
            return TemperatureReading(
                round(max(temperatures), 1),
                "Windows ACPI",
                "Leitura ACPI pode representar a zona termica, nao apenas a CPU.",
            )

        return TemperatureReading(None, "ACPI")


class TemperatureHistory:
    """Armazena leituras recentes para uma futura tela com grafico."""

    def __init__(self, limit: int = 120) -> None:
        self.limit = limit
        self.items: list[tuple[datetime, float]] = []

    def add(self, value_celsius: float | None) -> None:
        if value_celsius is None:
            return

        self.items.append((datetime.now(), value_celsius))
        self.items = self.items[-self.limit :]


class TemperatureMonitorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.provider = CpuTemperatureProvider()
        self.history = TemperatureHistory()

        self.temperature_var = tk.StringVar(value="--.- C")
        self.status_var = tk.StringVar(value="Iniciando leitura...")
        self.source_var = tk.StringVar(value="Fonte: --")

        self._configure_window()
        self._build_layout()
        self._schedule_update()

    def _configure_window(self) -> None:
        self.root.title("Monitor de Temperatura")
        self.root.geometry("360x220")
        self.root.minsize(320, 200)
        self.root.resizable(False, False)

    def _build_layout(self) -> None:
        main = ttk.Frame(self.root, padding=24)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main,
            text="Temperatura da CPU",
            font=("Segoe UI", 14, "bold"),
        ).pack(anchor="center")

        ttk.Label(
            main,
            textvariable=self.temperature_var,
            font=("Segoe UI", 34, "bold"),
        ).pack(anchor="center", pady=(18, 8))

        ttk.Label(
            main,
            textvariable=self.source_var,
            font=("Segoe UI", 9),
        ).pack(anchor="center")

        ttk.Label(
            main,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            wraplength=300,
            justify="center",
        ).pack(anchor="center", pady=(16, 0))

    def _schedule_update(self) -> None:
        self._update_temperature()
        self.root.after(UPDATE_INTERVAL_MS, self._schedule_update)

    def _update_temperature(self) -> None:
        reading = self.provider.read_cpu_temperature()
        self.history.add(reading.value_celsius)

        if reading.value_celsius is None:
            self.temperature_var.set("--.- C")
        else:
            self.temperature_var.set(f"{reading.value_celsius:.1f} C")

        self.source_var.set(f"Fonte: {reading.source}")
        self.status_var.set(reading.message or "Atualizado a cada 2 segundos.")

    # Ponto de extensao futuro: adicionar provider equivalente para GPU.
    def read_gpu_temperature(self) -> TemperatureReading:
        return TemperatureReading(None, "GPU", "Leitura de GPU ainda nao implementada.")


def main() -> None:
    root = tk.Tk()
    TemperatureMonitorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
