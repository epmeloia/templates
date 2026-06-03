# Decisões técnicas

Este arquivo registra decisões, tentativas, resultados e caminhos de reversão do projeto.

## 2026-06-03 - v01.00 - Projeto inicial

### Objetivo

Criar um aplicativo Python simples, com `tkinter`, para mostrar a temperatura atual da CPU no Windows 11.

### Decisão

Começar com a solução mais simples possível:

- Janela `tkinter`.
- Atualização a cada 2 segundos.
- Dependências Python em `requirements.txt`.
- Estrutura preparada para GPU e gráfico de histórico.

## 2026-06-03 - v01.01 - Dependências WMI

### Ocorrido

O app abriu corretamente, mas exibiu:

```txt
Fonte: Dependencia ausente
```

### Decisão

Instalar as dependências:

```powershell
cd "D:\_DEVOPS\Monitor_Temperatura"; py -3 -m pip install wmi==1.5.1 pywin32==311
```

### Observação

O `requirements.txt` inicial usava `pywin32==306`, mas o `pip` disponível no equipamento encontrou `pywin32==311`.

## 2026-06-03 - v01.02 - Tentativa com LibreHardwareMonitor

### Ocorrido

O Fan Control exibe temperatura da CPU usando:

```txt
Core Average - Intel Core i9-14900HX (C)
```

O arquivo do Fan Control indicou o sensor:

```txt
/intelcpu/0/temperature/1
```

### Decisão

Tentar ler diretamente a DLL:

```txt
D:\_INSTALADOS\FanControl\LibreHardwareMonitorLib.dll
```

Foi adicionada a dependência:

```txt
pythonnet==3.1.0
```

### Resultado

A DLL carregou corretamente e encontrou:

```txt
Intel Core i9-14900HX
/intelcpu/0/temperature/1
```

Porém todos os sensores de temperatura da CPU retornaram:

```txt
None
```

A GPU retornou temperatura pela mesma DLL, indicando que o problema ficou restrito à leitura da CPU.

### Como reverter

Remover a tentativa direta com `LibreHardwareMonitorLib.dll` do arquivo:

```txt
monitor-temperatura.py
```

E remover do `requirements.txt`:

```txt
pythonnet==3.1.0
```

## 2026-06-03 - v01.03 - Decisão por HWiNFO CSV

### Ocorrido

A leitura via WMI padrão e via LibreHardwareMonitor direto não retornou temperatura da CPU.

Também foi avaliada a opção de usar `Shared Memory Support` do HWiNFO, mas esse caminho é mais complexo e tem restrições de documentação/licença para implementação aberta.

### Decisão

Usar o HWiNFO como fonte intermediária, mas por meio de log CSV.

Caminho definido para o CSV:

```txt
D:\_DEVOPS\Monitor_Temperatura\hwinfo-log.csv
```

### Motivo

O CSV é mais simples, mais seguro para Python e não exige implementar diretamente a interface de memória compartilhada do HWiNFO.

### Alteração no app

O arquivo `monitor-temperatura.py` passa a tentar ler primeiro a última linha do CSV do HWiNFO.

Se o CSV ainda não existir, o app mostra uma mensagem informando o caminho esperado.

As leituras anteriores via LibreHardwareMonitor, WMI e ACPI permanecem como fallback.

### Próximos passos

1. Instalar HWiNFO.
2. Abrir o HWiNFO em modo de sensores.
3. Ativar o log dos sensores em CSV.
4. Salvar o log em:

```txt
D:\_DEVOPS\Monitor_Temperatura\hwinfo-log.csv
```

5. Executar novamente:

```powershell
cd "D:\_DEVOPS\Monitor_Temperatura"; py -3 .\monitor-temperatura.py
```

### Como reverter

Se HWiNFO CSV não funcionar ou não for desejado:

1. Remover a leitura por CSV do arquivo `monitor-temperatura.py`.
2. Voltar para a estratégia anterior.
3. Investigar novamente o Fan Control/LibreHardwareMonitor.

## 2026-06-03 - v01.04 - Ajuste do caminho do CSV do HWiNFO

### Ocorrido

O HWiNFO foi instalado em:

```txt
D:\_INSTALADOS\HWiNFO64
```

O log CSV foi configurado na pasta:

```txt
D:\_DEVOPS\Monitor_Temperatura\LogSensor\
```

Arquivo criado pelo HWiNFO:

```txt
D:\_DEVOPS\Monitor_Temperatura\LogSensor\hwinfo-log.csv
```

### Decisão

Atualizar o app para ler o CSV no novo caminho:

```txt
D:\_DEVOPS\Monitor_Temperatura\LogSensor\hwinfo-log.csv
```

Também foi ajustada a detecção da coluna de temperatura para considerar cabeçalhos em português do Brasil.

### Sensor identificado no CSV

A coluna preferencial encontrada foi:

```txt
Temperaturas centrais (avg) [°C]
```

### Como reverter

Se for necessário voltar para o caminho anterior, alterar a constante `HWINFO_CSV_PATH` em `monitor-temperatura.py` para:

```txt
D:\_DEVOPS\Monitor_Temperatura\hwinfo-log.csv
```

## 2026-06-03 - v01.05 - Monitoramento ampliado da CPU

### Ocorrido

Após validar a leitura principal com o HWiNFO CSV, foi decidido ampliar a tela para mostrar mais informações úteis para evitar travamentos, queda de desempenho ou desligamento por temperatura.

### Decisão

Manter `Temperaturas centrais (avg) [°C]` como leitura principal e adicionar quatro indicadores:

```txt
Núcleo máximo [°C]
CPU Inteira [°C]
Estrangulamento térmico do núcleo (avg) [Yes/No]
Limite de potência do núcleo excedido (avg) [Yes/No]
```

### Motivo

A média dos núcleos mostra a visão geral, mas o núcleo máximo e a CPU inteira ajudam a identificar picos. Os alertas de estrangulamento térmico e limite de potência indicam quando a CPU já está reduzindo desempenho ou batendo restrições operacionais.

### Como reverter

Se a tela ficar poluída ou alguma leitura não for útil, remover da interface os campos adicionais e manter apenas:

```txt
Temperaturas centrais (avg) [°C]
```
