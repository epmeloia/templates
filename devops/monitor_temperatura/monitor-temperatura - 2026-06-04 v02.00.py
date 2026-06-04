# ------------------------------------------
# monitor-temperatura.py
# ------------------------------------------
#
# ##----------####----------####----------##
#          .' '.    .' '.         ,-.
# .        .   .    .   .         \ /
#  .         .        .       . -{|||)<
#    ' .  . ' ' .  . ' ' . . '    / \
#                                 `-^
# ##----------####----------####----------##
#
# ------------------------------------------
# Desenvolvimento atraves do CHARTGPT\CODEX
# ------------------------------------------
#
# Versao:
#
# - 2026-06-04 v02.00
# - Titulos das secoes CPU e GPU alterados para azul neon.
# - Titulo GPU EXTERNA alterado para GPU NVIDEA.
#
# -----------------------------------
#

import csv
import json
import os
import re
import sys
import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from datetime import datetime


UPDATE_INTERVAL_MS = 2000
HWINFO_CSV_PATH = r"D:\_DEVOPS\Monitor_Temperatura\LogSensor\hwinfo-log.csv"
CONFIG_PATH = r"D:\_DEVOPS\Monitor_Temperatura\config-temperatura.json"
COLOR_OK = "#39ff14"
COLOR_WARNING = "#ffd400"
COLOR_DANGER = "#ff3333"
COLOR_BACKGROUND = "#050607"
COLOR_PANEL = "#101316"
COLOR_PANEL_BORDER = "#2b3138"
COLOR_NORMAL = "#eef3f8"
COLOR_MUTED = "#8b98a5"
COLOR_NEON_BLUE = "#00c8ff"
FAN_CONTROL_LIBRE_HARDWARE_MONITOR_DLL = (
    r"D:\_INSTALADOS\FanControl\LibreHardwareMonitorLib.dll"
)
CPU_SENSOR_IDENTIFIER = "/intelcpu/0/temperature/1"


@dataclass
class TemperatureReading:
    value_celsius: float | None
    source: str
    message: str = ""


@dataclass
class CpuMonitorReading:
    average_celsius: float | None
    max_celsius: float | None
    package_celsius: float | None
    thermal_throttling: str | None
    power_limit: str | None
    source: str
    message: str = ""


@dataclass
class GpuMonitorReading:
    temperature_celsius: float | None
    hot_spot_celsius: float | None
    memory_celsius: float | None
    usage_percent: float | None
    clock_mhz: float | None
    thermal_limit: str | None
    source: str
    message: str = ""


class TemperatureLimitConfig:
    DEFAULT_LIMITS = {
        "temperaturas_centrais_avg": {"amarelo": 80, "vermelho": 90},
        "nucleo_maximo": {"amarelo": 85, "vermelho": 95},
        "cpu_inteira": {"amarelo": 85, "vermelho": 95},
        "gpu_temperatura": {"amarelo": 80, "vermelho": 90},
        "gpu_hot_spot": {"amarelo": 90, "vermelho": 100},
        "gpu_memoria": {"amarelo": 90, "vermelho": 100},
    }

    def __init__(self, path: str = CONFIG_PATH) -> None:
        self.path = path
        self.limits = self._load_limits()

    def _load_limits(self) -> dict[str, dict[str, float]]:
        if not os.path.exists(self.path):
            return self.DEFAULT_LIMITS

        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception:
            return self.DEFAULT_LIMITS

        limits = self.DEFAULT_LIMITS.copy()
        for key, default_value in self.DEFAULT_LIMITS.items():
            item = data.get(key, {})
            limits[key] = {
                "amarelo": self._number_or_default(
                    item.get("amarelo"),
                    default_value["amarelo"],
                ),
                "vermelho": self._number_or_default(
                    item.get("vermelho"),
                    default_value["vermelho"],
                ),
            }

        return limits

    def _number_or_default(self, value, default: float) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return default

    def level_for(self, key: str, value: float | None) -> str:
        if value is None:
            return "normal"

        limits = self.limits.get(key, {})
        yellow = limits.get("amarelo", 80)
        red = limits.get("vermelho", 90)

        if value >= red:
            return "danger"
        if value >= yellow:
            return "warning"
        return "ok"


class CpuTemperatureProvider:
    """Busca a temperatura da CPU por HWiNFO CSV e usa outras fontes como fallback."""

    def __init__(self) -> None:
        self._wmi = None
        self._computer = None
        self._lhm_error = ""

        self._initialize_libre_hardware_monitor()
        self._initialize_wmi()

    def _initialize_libre_hardware_monitor(self) -> None:
        if not os.path.exists(FAN_CONTROL_LIBRE_HARDWARE_MONITOR_DLL):
            self._lhm_error = "DLL do LibreHardwareMonitor nao encontrada."
            return

        try:
            import clr

            sys.path.append(os.path.dirname(FAN_CONTROL_LIBRE_HARDWARE_MONITOR_DLL))
            clr.AddReference(FAN_CONTROL_LIBRE_HARDWARE_MONITOR_DLL)

            from LibreHardwareMonitor.Hardware import Computer

            computer = Computer()
            computer.IsCpuEnabled = True
            computer.IsGpuEnabled = False
            computer.IsMemoryEnabled = False
            computer.IsMotherboardEnabled = False
            computer.IsControllerEnabled = False
            computer.IsStorageEnabled = False
            computer.Open()

            self._computer = computer
        except Exception as error:
            self._computer = None
            self._lhm_error = f"Falha ao carregar LibreHardwareMonitor: {error}"

    def _initialize_wmi(self) -> None:
        try:
            import wmi

            self._wmi = wmi
        except ImportError:
            self._wmi = None

    def read_cpu_temperature(self) -> TemperatureReading:
        metrics = self.read_cpu_metrics()
        return TemperatureReading(
            metrics.average_celsius,
            metrics.source,
            metrics.message,
        )

    def read_cpu_metrics(self) -> CpuMonitorReading:
        metrics = self._read_hwinfo_csv_metrics()
        if metrics.average_celsius is not None:
            return metrics

        reading = self._read_hwinfo_csv()
        if reading.value_celsius is not None:
            return CpuMonitorReading(
                reading.value_celsius,
                None,
                None,
                None,
                None,
                reading.source,
                reading.message,
            )
        first_failure = reading

        reading = self._read_specific_libre_hardware_monitor_sensor()
        if reading.value_celsius is not None:
            return CpuMonitorReading(
                reading.value_celsius,
                None,
                None,
                None,
                None,
                reading.source,
                reading.message,
            )

        reading = self._read_hardware_monitor_wmi()
        if reading.value_celsius is not None:
            return CpuMonitorReading(
                reading.value_celsius,
                None,
                None,
                None,
                None,
                reading.source,
                reading.message,
            )

        reading = self._read_acpi_thermal_zone()
        if reading.value_celsius is not None:
            return CpuMonitorReading(
                reading.value_celsius,
                None,
                None,
                None,
                None,
                reading.source,
                reading.message,
            )

        return CpuMonitorReading(
            None,
            None,
            None,
            None,
            None,
            first_failure.source or "Indisponivel",
            first_failure.message or "Nenhum sensor de CPU foi encontrado.",
        )

    def read_gpu_metrics(self) -> GpuMonitorReading:
        if not os.path.exists(HWINFO_CSV_PATH):
            return GpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                f"Configure o log do HWiNFO em: {HWINFO_CSV_PATH}",
            )

        try:
            rows = self._read_csv_rows(HWINFO_CSV_PATH)
        except Exception as error:
            return GpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                f"Falha ao ler CSV da GPU: {error}",
            )

        if len(rows) < 2:
            return GpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                "CSV sem dados suficientes para GPU.",
            )

        header = rows[0]
        data_row = self._last_data_row(rows[1:])
        if data_row is None:
            return GpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                "CSV sem linha de leitura da GPU.",
            )

        temperature = self._read_named_temperature(
            header,
            data_row,
            ("temperatura gpu", "gpu temperature"),
        )
        hot_spot = self._read_named_temperature(
            header,
            data_row,
            ("temperatura de ponto quente da gpu", "gpu hot spot", "gpu hotspot"),
        )
        memory = self._read_named_temperature(
            header,
            data_row,
            (
                "temperatura de juncao da memoria gpu",
                "temperatura de junção da memória gpu",
                "temperatura de junÃ§Ã£o da memÃ³ria gpu",
                "gpu memory junction",
            ),
        )
        usage = self._read_named_number(
            header,
            data_row,
            (
                "carga do nucleo da gpu",
                "carga do núcleo da gpu",
                "carga do nÃºcleo da gpu",
                "gpu core load",
                "gpu usage",
                "uso total da gpu",
            ),
        )
        clock = self._read_named_number(
            header,
            data_row,
            ("gpu clock", "relogio da gpu", "relógio da gpu"),
        )
        thermal_limit = self._read_named_text(
            header,
            data_row,
            (
                "limite de desempenho - termico",
                "limite de desempenho - térmico",
                "limite de desempenho - tÃ©rmico",
                "performance limit - thermal",
            ),
        )

        if temperature is None and hot_spot is None and memory is None:
            return GpuMonitorReading(
                None,
                None,
                None,
                usage,
                clock,
                thermal_limit,
                "HWiNFO CSV",
                "Colunas de temperatura da GPU nao foram encontradas.",
            )

        return GpuMonitorReading(
            temperature,
            hot_spot,
            memory,
            None if usage is None else round(usage, 1),
            None if clock is None else round(clock, 1),
            thermal_limit,
            "HWiNFO CSV",
            "Atualizado a cada 2 segundos.",
        )

    def _read_hwinfo_csv_metrics(self) -> CpuMonitorReading:
        if not os.path.exists(HWINFO_CSV_PATH):
            return CpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                f"Configure o log do HWiNFO em: {HWINFO_CSV_PATH}",
            )

        try:
            rows = self._read_csv_rows(HWINFO_CSV_PATH)
        except Exception as error:
            return CpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                f"Falha ao ler CSV: {error}",
            )

        if len(rows) < 2:
            return CpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                "CSV sem dados suficientes.",
            )

        header = rows[0]
        data_row = self._last_data_row(rows[1:])
        if data_row is None:
            return CpuMonitorReading(
                None,
                None,
                None,
                None,
                None,
                "HWiNFO CSV",
                "CSV sem linha de leitura.",
            )

        average = self._read_named_temperature(header, data_row, ("temperaturas centrais (avg)", "core average"))
        max_core = self._read_named_temperature(header, data_row, ("nucleo maximo", "nÃºcleo mÃ¡ximo", "core max"))
        package = self._read_named_temperature(header, data_row, ("cpu inteira", "cpu package"))
        thermal = self._read_named_text(header, data_row, ("estrangulamento termico do nucleo (avg)", "estrangulamento térmico do núcleo (avg)", "estrangulamento tÃ©rmico do nÃºcleo (avg)", "thermal throttling"))
        power = self._read_named_text(header, data_row, ("limite de potencia do nucleo excedido (avg)", "limite de potência do núcleo excedido (avg)", "limite de potÃªncia do nÃºcleo excedido (avg)", "power limit"))

        if average is None:
            return CpuMonitorReading(
                None,
                max_core,
                package,
                thermal,
                power,
                "HWiNFO CSV",
                "Coluna de temperatura media da CPU nao foi encontrada.",
            )

        return CpuMonitorReading(
            average,
            max_core,
            package,
            thermal,
            power,
            "HWiNFO CSV",
            "Atualizado a cada 2 segundos.",
        )

    def _read_hwinfo_csv(self) -> TemperatureReading:
        if not os.path.exists(HWINFO_CSV_PATH):
            return TemperatureReading(
                None,
                "HWiNFO CSV",
                f"Configure o log do HWiNFO em: {HWINFO_CSV_PATH}",
            )

        try:
            rows = self._read_csv_rows(HWINFO_CSV_PATH)
        except Exception as error:
            return TemperatureReading(None, "HWiNFO CSV", f"Falha ao ler CSV: {error}")

        if len(rows) < 2:
            return TemperatureReading(None, "HWiNFO CSV", "CSV sem dados suficientes.")

        header = rows[0]
        data_row = self._last_data_row(rows[1:])
        if data_row is None:
            return TemperatureReading(None, "HWiNFO CSV", "CSV sem linha de leitura.")

        sensor_index = self._find_cpu_temperature_column(header)
        if sensor_index is None:
            return TemperatureReading(
                None,
                "HWiNFO CSV",
                "Nenhuma coluna de temperatura da CPU foi encontrada no CSV.",
            )

        if sensor_index >= len(data_row):
            return TemperatureReading(
                None,
                "HWiNFO CSV",
                "Linha mais recente nao possui a coluna de temperatura esperada.",
            )

        value = self._parse_temperature_value(data_row[sensor_index])
        if value is None:
            return TemperatureReading(
                None,
                "HWiNFO CSV",
                f"Valor invalido na coluna: {header[sensor_index]}",
            )

        return TemperatureReading(
            round(value, 1),
            "HWiNFO CSV",
            f"Sensor: {header[sensor_index]}",
        )

    def _read_csv_rows(self, path: str) -> list[list[str]]:
        for encoding in ("utf-8-sig", "cp1252"):
            try:
                with open(path, "r", encoding=encoding, newline="") as file:
                    return list(csv.reader(file))
            except UnicodeDecodeError:
                continue

        with open(path, "r", newline="") as file:
            return list(csv.reader(file))

    def _last_data_row(self, rows: list[list[str]]) -> list[str] | None:
        for row in reversed(rows):
            if row and any(cell.strip() for cell in row):
                first_cell = row[0].strip().lower()
                if first_cell not in ("date", "data"):
                    return row

        return None

    def _find_cpu_temperature_column(self, header: list[str]) -> int | None:
        preferred_terms = (
            "temperaturas centrais (avg)",
            "core average",
            "cpu inteira",
            "cpu package",
            "nucleo maximo",
            "núcleo máximo",
            "core max",
            "cpu temperature",
            "cpu",
        )

        candidates: list[tuple[int, int]] = []
        for index, column_name in enumerate(header):
            normalized = column_name.lower()
            if "gpu" in normalized:
                continue
            if not self._looks_like_temperature_column(normalized):
                continue

            score = 0
            for position, term in enumerate(preferred_terms):
                if term in normalized:
                    score = len(preferred_terms) - position
                    break

            candidates.append((score, index))

        if not candidates:
            return None

        candidates.sort(reverse=True)
        return candidates[0][1]

    def _find_column_by_terms(self, header: list[str], terms: tuple[str, ...]) -> int | None:
        normalized_terms = tuple(term.lower() for term in terms)
        for index, column_name in enumerate(header):
            normalized = column_name.lower()
            if any(term in normalized for term in normalized_terms):
                return index

        return None

    def _read_named_temperature(
        self,
        header: list[str],
        data_row: list[str],
        terms: tuple[str, ...],
    ) -> float | None:
        index = self._find_column_by_terms(header, terms)
        if index is None or index >= len(data_row):
            return None

        value = self._parse_temperature_value(data_row[index])
        if value is None:
            return None

        return round(value, 1)

    def _read_named_number(
        self,
        header: list[str],
        data_row: list[str],
        terms: tuple[str, ...],
    ) -> float | None:
        index = self._find_column_by_terms(header, terms)
        if index is None or index >= len(data_row):
            return None

        return self._parse_temperature_value(data_row[index])

    def _read_named_text(
        self,
        header: list[str],
        data_row: list[str],
        terms: tuple[str, ...],
    ) -> str | None:
        index = self._find_column_by_terms(header, terms)
        if index is None or index >= len(data_row):
            return None

        value = data_row[index].strip()
        return value or None

    def _looks_like_temperature_column(self, column_name: str) -> bool:
        temperature_terms = (
            "temperature",
            "temperatura",
            "temperaturas",
            "temp",
            "core",
            "nucleo",
            "núcleo",
            "package",
            "cpu",
        )
        celsius_terms = ("c", "°c", "degc")
        has_temperature_term = any(term in column_name for term in temperature_terms)
        has_celsius_term = any(term in column_name for term in celsius_terms)
        return has_temperature_term and has_celsius_term

    def _parse_temperature_value(self, value: str) -> float | None:
        match = re.search(r"-?\d+(?:[.,]\d+)?", value)
        if not match:
            return None

        try:
            return float(match.group(0).replace(",", "."))
        except ValueError:
            return None

    def _read_specific_libre_hardware_monitor_sensor(self) -> TemperatureReading:
        if self._computer is None:
            return TemperatureReading(None, "LibreHardwareMonitor", self._lhm_error)

        try:
            for hardware in self._computer.Hardware:
                hardware.Update()
                reading = self._find_sensor_in_hardware(hardware)
                if reading.value_celsius is not None:
                    return reading

                for subhardware in hardware.SubHardware:
                    subhardware.Update()
                    reading = self._find_sensor_in_hardware(subhardware)
                    if reading.value_celsius is not None:
                        return reading
        except Exception as error:
            return TemperatureReading(
                None,
                "LibreHardwareMonitor",
                f"Falha ao ler sensor especifico: {error}",
            )

        return TemperatureReading(
            None,
            "LibreHardwareMonitor",
            f"Sensor nao encontrado: {CPU_SENSOR_IDENTIFIER}",
        )

    def _find_sensor_in_hardware(self, hardware) -> TemperatureReading:
        for sensor in hardware.Sensors:
            identifier = str(sensor.Identifier)
            value = sensor.Value

            if identifier == CPU_SENSOR_IDENTIFIER and value is not None:
                return TemperatureReading(
                    round(float(value), 1),
                    "LibreHardwareMonitor",
                    f"Sensor: {CPU_SENSOR_IDENTIFIER}",
                )

        return TemperatureReading(None, "LibreHardwareMonitor")

    def _read_hardware_monitor_wmi(self) -> TemperatureReading:
        if self._wmi is None:
            return TemperatureReading(
                None,
                "Dependencia ausente",
                "Instale as dependencias com: pip install -r requirements.txt",
            )

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
        if self._wmi is None:
            return TemperatureReading(None, "ACPI")

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


class TemperatureValueCanvas(tk.Canvas):
    def __init__(
        self,
        parent: tk.Widget,
        width: int = 96,
        suffix: str = "C",
        font_size: int = 20,
    ) -> None:
        super().__init__(
            parent,
            width=width,
            height=32,
            bg=COLOR_PANEL,
            bd=0,
            highlightthickness=0,
        )
        self.canvas_width = width
        self.suffix = suffix
        self.font_size = font_size
        self.value = "--"
        self.current_fg = COLOR_NORMAL
        self.alert_level = "normal"
        self._draw()

    def set_value(self, value: str) -> None:
        self.value = value
        self._draw()

    def set_fg(self, color: str) -> None:
        self.current_fg = color
        self._draw()

    def _draw(self) -> None:
        self.delete("all")
        font = ("Consolas", self.font_size, "bold")
        unit_font = ("Consolas", self.font_size, "bold")
        center_x = self.canvas_width // 2 - (4 if self.suffix else 0)
        y = 17

        if self.value == "--" or not self.suffix:
            self.create_text(
                self.canvas_width // 2,
                y,
                text=self.value,
                font=font,
                fill=self.current_fg,
                anchor="center",
            )
            return

        number_item = self.create_text(
            center_x,
            y,
            text=self.value,
            font=font,
            fill=self.current_fg,
            anchor="center",
        )
        self.update_idletasks()
        bbox = self.bbox(number_item)
        if bbox is None:
            return

        self.create_text(
            bbox[2] - 1,
            y,
            text=self.suffix,
            font=unit_font,
            fill=self.current_fg,
            anchor="w",
        )


class TemperatureMonitorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.provider = CpuTemperatureProvider()
        self.limit_config = TemperatureLimitConfig()
        self.history = TemperatureHistory()
        self.blink_visible = True

        self.temperature_var = tk.StringVar(value="--.-")
        self.max_temperature_var = tk.StringVar(value="--")
        self.package_temperature_var = tk.StringVar(value="--")
        self.thermal_throttling_var = tk.StringVar(value="--")
        self.power_limit_var = tk.StringVar(value="--")
        self.gpu_temperature_var = tk.StringVar(value="--")
        self.gpu_hot_spot_var = tk.StringVar(value="--")
        self.gpu_memory_var = tk.StringVar(value="--")
        self.gpu_usage_var = tk.StringVar(value="--")
        self.gpu_clock_var = tk.StringVar(value="--")
        self.gpu_thermal_limit_var = tk.StringVar(value="--")
        self.status_var = tk.StringVar(value="Iniciando leitura...")
        self.source_var = tk.StringVar(value="Fonte: --")
        self.temperature_label: TemperatureValueCanvas | None = None
        self.max_temperature_label: TemperatureValueCanvas | None = None
        self.package_temperature_label: TemperatureValueCanvas | None = None
        self.gpu_temperature_label: TemperatureValueCanvas | None = None
        self.gpu_hot_spot_label: TemperatureValueCanvas | None = None
        self.gpu_memory_label: TemperatureValueCanvas | None = None
        self.gpu_usage_label: TemperatureValueCanvas | None = None
        self.gpu_clock_label: TemperatureValueCanvas | None = None
        self.gpu_thermal_limit_label: TemperatureValueCanvas | None = None

        self._configure_window()
        self._configure_styles()
        self._build_layout()
        self._schedule_update()
        self._schedule_blink()

    def _configure_window(self) -> None:
        self.root.title("Monitor de Temperatura")
        self.root.geometry("330x390")
        self.root.minsize(330, 390)
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)
        self.root.configure(bg=COLOR_BACKGROUND)

    def _configure_styles(self) -> None:
        style = ttk.Style()
        style.configure("Dark.TFrame", background=COLOR_BACKGROUND)

    def _build_layout(self) -> None:
        main = tk.Frame(self.root, bg=COLOR_BACKGROUND, padx=10, pady=9)
        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text="MONITOR DE TEMPERATURA",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_MUTED,
            bg=COLOR_BACKGROUND,
        ).pack(anchor="center")

        tk.Label(
            main,
            textvariable=self.source_var,
            font=("Segoe UI", 8),
            fg=COLOR_MUTED,
            bg=COLOR_BACKGROUND,
        ).pack(anchor="center", pady=(2, 0))

        tk.Label(
            main,
            text="CPU",
            font=("Segoe UI", 8, "bold"),
            fg=COLOR_NEON_BLUE,
            bg=COLOR_BACKGROUND,
        ).pack(anchor="center", pady=(7, 0))

        temperature_panel = tk.Frame(
            main,
            bg=COLOR_PANEL,
            highlightbackground=COLOR_PANEL_BORDER,
            highlightcolor=COLOR_PANEL_BORDER,
            highlightthickness=1,
            padx=4,
            pady=4,
        )
        temperature_panel.pack(anchor="center", fill="x", pady=(3, 0))

        self.temperature_label = self._add_temperature_card(
            temperature_panel, "Media", self.temperature_var, 0, 0
        )
        self.max_temperature_label = self._add_temperature_card(
            temperature_panel, "Nucleo maximo", self.max_temperature_var, 0, 1
        )
        self.package_temperature_label = self._add_temperature_card(
            temperature_panel, "CPU Inteira", self.package_temperature_var, 0, 2
        )
        for column in range(3):
            temperature_panel.grid_columnconfigure(column, weight=1, uniform="temps")

        status_panel = tk.Frame(main, bg=COLOR_BACKGROUND)
        status_panel.pack(anchor="center", fill="x", pady=(8, 0))
        self._add_status_row(
            status_panel, "Estrangulamento termico", self.thermal_throttling_var, 0
        )
        self._add_status_row(
            status_panel, "Limite de potencia", self.power_limit_var, 1
        )

        tk.Label(
            main,
            text="GPU NVIDEA",
            font=("Segoe UI", 8, "bold"),
            fg=COLOR_NEON_BLUE,
            bg=COLOR_BACKGROUND,
        ).pack(anchor="center", pady=(8, 0))

        gpu_panel = tk.Frame(
            main,
            bg=COLOR_PANEL,
            highlightbackground=COLOR_PANEL_BORDER,
            highlightcolor=COLOR_PANEL_BORDER,
            highlightthickness=1,
            padx=4,
            pady=4,
        )
        gpu_panel.pack(anchor="center", fill="x", pady=(3, 0))

        self.gpu_temperature_label = self._add_temperature_card(
            gpu_panel, "GPU", self.gpu_temperature_var, 0, 0
        )
        self.gpu_hot_spot_label = self._add_temperature_card(
            gpu_panel, "Hot Spot", self.gpu_hot_spot_var, 0, 1
        )
        self.gpu_memory_label = self._add_temperature_card(
            gpu_panel, "Memoria", self.gpu_memory_var, 0, 2
        )
        self.gpu_usage_label = self._add_temperature_card(
            gpu_panel, "Uso", self.gpu_usage_var, 1, 0, "%"
        )
        self.gpu_clock_label = self._add_temperature_card(
            gpu_panel, "Clock", self.gpu_clock_var, 1, 1, "MHz"
        )
        self.gpu_thermal_limit_label = self._add_temperature_card(
            gpu_panel, "Termico", self.gpu_thermal_limit_var, 1, 2, ""
        )
        for column in range(3):
            gpu_panel.grid_columnconfigure(column, weight=1, uniform="gpu")

        tk.Label(
            main,
            textvariable=self.status_var,
            font=("Segoe UI", 8),
            wraplength=300,
            justify="center",
            fg=COLOR_MUTED,
            bg=COLOR_BACKGROUND,
        ).pack(anchor="center", pady=(8, 0))

    def _add_temperature_card(
        self,
        parent: tk.Frame,
        label_text: str,
        value_var: tk.StringVar,
        row: int,
        column: int,
        suffix: str = "C",
    ) -> TemperatureValueCanvas:
        card = tk.Frame(parent, bg=COLOR_PANEL, padx=2, pady=1)
        card.grid(row=row, column=column, sticky="nsew", padx=2, pady=1)

        tk.Label(
            card,
            text=label_text,
            font=("Segoe UI", 8),
            fg=COLOR_MUTED,
            bg=COLOR_PANEL,
        ).pack(anchor="center")

        font_size = 15 if row > 0 or suffix == "" else 20
        value_label = TemperatureValueCanvas(card, suffix=suffix, font_size=font_size)
        value_label.pack(anchor="center", pady=(2, 0))
        value_var.trace_add(
            "write",
            lambda *_args, target=value_label, source=value_var: target.set_value(
                source.get()
            ),
        )
        return value_label

    def _add_status_row(
        self,
        parent: tk.Frame,
        label_text: str,
        value_var: tk.StringVar,
        row: int,
    ) -> None:
        tk.Label(
            parent,
            text=label_text,
            font=("Segoe UI", 8),
            fg=COLOR_MUTED,
            bg=COLOR_BACKGROUND,
        ).grid(row=row, column=0, sticky="e", padx=(0, 8), pady=1)

        tk.Label(
            parent,
            textvariable=value_var,
            font=("Consolas", 8, "bold"),
            fg=COLOR_NORMAL,
            bg=COLOR_BACKGROUND,
            width=8,
            anchor="w",
        ).grid(row=row, column=1, sticky="w", pady=1)

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

    def _schedule_update(self) -> None:
        self._update_temperature()
        self.root.after(UPDATE_INTERVAL_MS, self._schedule_update)

    def _schedule_blink(self) -> None:
        self.blink_visible = not self.blink_visible
        self._refresh_blinking_labels()
        self.root.after(500, self._schedule_blink)

    def _update_temperature(self) -> None:
        reading = self.provider.read_cpu_metrics()
        gpu_reading = self.provider.read_gpu_metrics()
        self.history.add(reading.average_celsius)

        if reading.average_celsius is None:
            self.temperature_var.set("--.-")
        else:
            self.temperature_var.set(f"{reading.average_celsius:.1f}")

        self.max_temperature_var.set(self._format_temperature(reading.max_celsius))
        self.package_temperature_var.set(self._format_temperature(reading.package_celsius))
        self.thermal_throttling_var.set(self._format_status(reading.thermal_throttling))
        self.power_limit_var.set(self._format_status(reading.power_limit))
        self.gpu_temperature_var.set(self._format_temperature(gpu_reading.temperature_celsius))
        self.gpu_hot_spot_var.set(self._format_temperature(gpu_reading.hot_spot_celsius))
        self.gpu_memory_var.set(self._format_temperature(gpu_reading.memory_celsius))
        self.gpu_usage_var.set(self._format_metric(gpu_reading.usage_percent))
        self.gpu_clock_var.set(self._format_metric(gpu_reading.clock_mhz))
        self.gpu_thermal_limit_var.set(self._format_status(gpu_reading.thermal_limit))

        self.source_var.set(f"Fonte: {reading.source}")
        self.status_var.set(reading.message or "Atualizado a cada 2 segundos.")
        self._apply_temperature_styles(reading, gpu_reading)

    def _format_temperature(self, value: float | None) -> str:
        if value is None:
            return "--"

        return f"{value:.1f}"

    def _format_metric(self, value: float | None) -> str:
        if value is None:
            return "--"

        if value >= 100:
            return f"{value:.0f}"

        return f"{value:.1f}"

    def _format_status(self, value: str | None) -> str:
        if value is None:
            return "--"

        normalized = value.strip().lower()
        if normalized in ("yes", "sim", "s"):
            return "SIM"
        if normalized in ("no", "nao", "não", "nÃ£o", "n"):
            return "Nao"

        return value

    def _apply_temperature_styles(
        self,
        reading: CpuMonitorReading,
        gpu_reading: GpuMonitorReading,
    ) -> None:
        self._set_temperature_style(
            self.temperature_label,
            self.limit_config.level_for(
                "temperaturas_centrais_avg",
                reading.average_celsius,
            ),
        )
        self._set_temperature_style(
            self.max_temperature_label,
            self.limit_config.level_for("nucleo_maximo", reading.max_celsius),
        )
        self._set_temperature_style(
            self.package_temperature_label,
            self.limit_config.level_for("cpu_inteira", reading.package_celsius),
        )
        self._set_temperature_style(
            self.gpu_temperature_label,
            self.limit_config.level_for(
                "gpu_temperatura",
                gpu_reading.temperature_celsius,
            ),
        )
        self._set_temperature_style(
            self.gpu_hot_spot_label,
            self.limit_config.level_for("gpu_hot_spot", gpu_reading.hot_spot_celsius),
        )
        self._set_temperature_style(
            self.gpu_memory_label,
            self.limit_config.level_for("gpu_memoria", gpu_reading.memory_celsius),
        )
        self._set_temperature_style(self.gpu_usage_label, "ok")
        self._set_temperature_style(self.gpu_clock_label, "normal")
        self._set_temperature_style(
            self.gpu_thermal_limit_label,
            self._status_level(gpu_reading.thermal_limit),
        )

    def _status_level(self, value: str | None) -> str:
        if value is None:
            return "normal"

        normalized = self._format_status(value).lower()
        if normalized == "sim":
            return "danger"
        if normalized == "nao":
            return "ok"

        return "normal"

    def _set_temperature_style(
        self,
        label: TemperatureValueCanvas | None,
        level: str,
    ) -> None:
        if label is None:
            return

        label.alert_level = level
        if level == "danger":
            label.set_fg(COLOR_DANGER if self.blink_visible else COLOR_PANEL)
        elif level == "warning":
            label.set_fg(COLOR_WARNING)
        elif level == "ok":
            label.set_fg(COLOR_OK)
        else:
            label.set_fg(COLOR_NORMAL)

    def _refresh_blinking_labels(self) -> None:
        for label in (
            self.temperature_label,
            self.max_temperature_label,
            self.package_temperature_label,
            self.gpu_temperature_label,
            self.gpu_hot_spot_label,
            self.gpu_memory_label,
            self.gpu_thermal_limit_label,
        ):
            if label is not None and getattr(label, "alert_level", "") == "danger":
                label.set_fg(COLOR_DANGER if self.blink_visible else COLOR_PANEL)


def main() -> None:
    root = tk.Tk()
    TemperatureMonitorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
