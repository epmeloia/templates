import os
import sys
import time


DLL_PATH = r"D:\_INSTALADOS\FanControl\LibreHardwareMonitorLib.dll"


def main() -> None:
    if not os.path.exists(DLL_PATH):
        print(f"DLL nao encontrada: {DLL_PATH}")
        return

    try:
        import clr

        sys.path.append(os.path.dirname(DLL_PATH))
        clr.AddReference(DLL_PATH)

        from LibreHardwareMonitor.Hardware import Computer
    except Exception as error:
        print(f"Falha ao carregar LibreHardwareMonitor: {error}")
        return

    computer = Computer()
    computer.IsCpuEnabled = True
    computer.IsGpuEnabled = False
    computer.IsMemoryEnabled = False
    computer.IsMotherboardEnabled = False
    computer.IsControllerEnabled = False
    computer.IsStorageEnabled = False
    computer.Open()

    print("Diagnostico de sensores de temperatura da CPU")
    print(f"DLL: {DLL_PATH}")
    print("Atualizando leituras por 20 segundos...")
    print()

    for attempt in range(1, 11):
        print(f"Tentativa {attempt}/10")

        found_temperature_sensor = False
        for hardware in computer.Hardware:
            hardware.Update()

            if str(hardware.Identifier) != "/intelcpu/0":
                continue

            print(f"Hardware: {hardware.Name} | {hardware.Identifier}")

            for sensor in hardware.Sensors:
                if str(sensor.SensorType) != "Temperature":
                    continue

                found_temperature_sensor = True
                print(
                    f"  {sensor.Name} | {sensor.Identifier} | Valor: {sensor.Value}"
                )

        if not found_temperature_sensor:
            print("  Nenhum sensor de temperatura de CPU foi encontrado.")

        print()
        time.sleep(2)

    computer.Close()


if __name__ == "__main__":
    main()
