#
# ##----------####----------####----------##
#          .' '.    .' '.         ,-.
# .        .   .    .   .         \ /
#  .         .        .       . -{|||)<
#    ' .  . ' ' .  . ' ' . . '    / \
#                                 `-^
# ##----------####----------####----------##
#

# Monitor de Temperatura

Projeto Python simples para Windows 11 que abre uma janela `tkinter` e atualiza a temperatura da CPU a cada 2 segundos.

## Arquivos

- `monitor-temperatura.py`: aplicacao principal.
- `requirements.txt`: dependencias Python.
- `README.md`: instrucoes do projeto.

## Como executar

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python .\monitor-temperatura.py
```

## Observacao sobre sensores no Windows

O Windows nem sempre expoe a temperatura real da CPU diretamente. O aplicativo tenta ler, nesta ordem:

1. Sensores publicados via LibreHardwareMonitor ou OpenHardwareMonitor.
2. Zona termica ACPI do Windows.

Para uma leitura mais confiavel da CPU, execute o LibreHardwareMonitor em segundo plano com o servidor WMI habilitado.

## Preparado para evolucao

A estrutura ja inclui pontos simples para adicionar:

- Temperatura da GPU.
- Grafico de historico usando os dados guardados em `TemperatureHistory`.


