#
# ##----------####----------####----------##
#          .' '.    .' '.         ,-.
# .        .   .    .   .         \ /
#  .         .        .       . -{|||)<
#    ' .  . ' ' .  . ' ' . . '    / \
#                                 `-^
# ##----------####----------####----------##
#

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

## 2026-06-03 - v01.06 - Limites visuais por JSON

### Ocorrido

Foi solicitada uma configuração externa para definir limites aceitáveis de temperatura e mudar a cor dos valores na interface.

### Decisão

Criar o arquivo:

```txt
config-temperatura.json
```

Com faixas por temperatura:

```json
{
  "temperaturas_centrais_avg": {
    "amarelo": 80,
    "vermelho": 90
  },
  "nucleo_maximo": {
    "amarelo": 85,
    "vermelho": 95
  },
  "cpu_inteira": {
    "amarelo": 85,
    "vermelho": 95
  }
}
```

### Comportamento

- Verde neon: abaixo do limite amarelo.
- Amarelo: igual ou acima do limite amarelo.
- Vermelho piscando: igual ou acima do limite vermelho.

### Como reverter

Remover o carregamento de `config-temperatura.json` e voltar os `ttk.Label` para estilo visual fixo.

## 2026-06-03 - v01.07 - Assinatura institucional

### Ocorrido

Foi solicitada a inclusão da assinatura institucional nos arquivos ativos em que isso não cause problema técnico.

### Decisão

Aplicar a assinatura nos arquivos ativos `.py` e `.md`.

Arquivos incluídos:

```txt
monitor-temperatura.py
diagnostico_sensores_cpu.py
README.md
DECISOES.md
app_monitor-temperatura_python_chatgpt.md
```

### Preservação

As cópias históricas versionadas de `monitor-temperatura.py` não foram alteradas, para manter o conteúdo fiel ao estado original de cada versão.

### Como reverter

Remover o bloco da assinatura dos arquivos ativos listados acima.

## 2026-06-03 - v01.08 - Painel escuro

### Ocorrido

Foi solicitada uma melhoria visual para deixar o fundo preto e apresentar os números de forma mais profissional e prática.

### Decisão

Atualizar a janela para um painel escuro:

- Fundo preto.
- Valor principal em destaque com fonte monoespaçada.
- Métricas secundárias em linhas, com nome à esquerda e valor à direita.
- Cores de alerta preservadas a partir de `config-temperatura.json`.
- Pisca vermelho mantido para valores acima do limite vermelho.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.07.py
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

## 2026-06-03 - v01.09 - Temperaturas lado a lado

### Ocorrido

Foi solicitado colocar as temperaturas uma ao lado da outra.

### Decisão

Organizar as três leituras de temperatura em cartões horizontais:

```txt
Média
Núcleo máximo
CPU Inteira
```

Os alertas de estrangulamento térmico e limite de potência foram mantidos abaixo das temperaturas, porque são estados operacionais e não leituras de temperatura.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.08.py
```

## 2026-06-03 - v01.10 - Layout compacto pelo template

### Ocorrido

Foi enviado um anexo como referência visual para reduzir o tamanho da janela e reposicionar as informações.

### Decisão

Compactar a interface mantendo:

```txt
Título centralizado
Fonte do sensor abaixo do título
Três temperaturas lado a lado
Alertas centralizados abaixo das temperaturas
Rodapé com status de atualização
```

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.09.py
```

## 2026-06-03 - v01.11 - Espaçamento da unidade Celsius

### Ocorrido

Foi observado que a distância entre o último número da temperatura e a letra `C` estava grande demais.

### Decisão

Remover o espaço entre o valor e a unidade:

```txt
60.0 C -> 60.0C
```

### Como reverter

Voltar a formatação de temperatura para:

```txt
{valor:.1f} C
```

## 2026-06-03 - v01.12 - Unidade Celsius colada visualmente

### Ocorrido

Mesmo sem espaço no texto, a fonte ainda deixava a letra `C` visualmente afastada do último número.

### Decisão

Desenhar a temperatura em um `Canvas`, posicionando o número e a letra `C` separadamente para deixar a unidade visualmente colada ao valor.

### Como reverter

Voltar para a formatação simples em `tk.Label`:

```txt
{valor:.1f}C
```

## 2026-06-03 - v01.13 - Monitoramento da GPU externa

### Ocorrido

Foi solicitado visualizar a temperatura da placa de vídeo externa, duplicando para baixo o padrão visual usado na CPU.

### Decisão

Adicionar uma segunda área compacta para a GPU externa, com seis leituras em duas linhas:

```txt
Temperatura da GPU
Hot Spot da GPU
Temperatura da memória da GPU
Uso da GPU
Velocidade da ventoinha da GPU
Limite térmico / Thermal Throttling da GPU
```

### Fonte

As leituras continuam usando o mesmo CSV do HWiNFO:

```txt
D:\_DEVOPS\Monitor_Temperatura\LogSensor\hwinfo-log.csv
```

### Observação

Se algum sensor não estiver sendo gravado no CSV, o campo aparece como `--`, sem interromper a janela.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.12.py
```

## 2026-06-03 - v01.14 - Janela sempre visível e FAN da GPU

### Ocorrido

Foi observado que o campo `Fan` da GPU não estava sendo atualizado.

### Análise

Foi feita busca no CSV do HWiNFO por colunas relacionadas a:

```txt
fan
ventoinha
rpm
pwm
cooler
```

Nenhuma coluna de ventoinha foi encontrada no log atual.

### Decisão

Manter o campo `Fan`, mas exibir:

```txt
Sem log
```

quando o HWiNFO não estiver gravando esse sensor no CSV.

Também foi configurada a janela para ficar sempre visível sobre outras janelas.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.13.py
```

## 2026-06-03 - v01.15 - Substituição de FAN por Clock da GPU

### Ocorrido

Como o CSV atual do HWiNFO não possui coluna de ventoinha da GPU, foi escolhida a opção `Clock da GPU` para substituir o campo `Fan`.

### Decisão

Remover o campo visual `Fan` da GPU e exibir:

```txt
Clock
```

com leitura em `MHz`, usando a coluna:

```txt
GPU Clock [MHz]
```

### Motivo

O clock ajuda a identificar queda de desempenho quando a GPU reduz frequência por temperatura, energia ou limitação térmica.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.14.py
```

## 2026-06-03 - v01.16 - Cabeçalho reduzido no arquivo Python

### Ocorrido

Foi solicitado reduzir a quantidade de informação histórica dentro do arquivo `monitor-temperatura.py`.

### Decisão

O topo do arquivo Python passa a manter apenas:

```txt
Versão atual
O que foi feito nessa versão
Referência ao DECISOES.md para histórico detalhado
```

### Motivo

O histórico completo já é registrado no arquivo:

```txt
DECISOES.md
```

Assim o código principal fica menor e mais fácil de ler.

### Regra daqui em diante

Registrar detalhes, contexto, motivo e reversão no `DECISOES.md`.

No topo do `.py`, manter apenas o versionamento atual e uma descrição curta.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.15.py
```

## 2026-06-04 - v02.00 - Títulos de seção em azul neon

### Ocorrido

Foi solicitado alterar a cor dos títulos `CPU` e `GPU EXTERNA` para azul neon.

Também foi solicitada a troca do texto:

```txt
GPU EXTERNA
```

para:

```txt
GPU NVIDEA
```

### Decisão

Adicionar a cor:

```txt
COLOR_NEON_BLUE = "#00c8ff"
```

e usar essa cor somente nos títulos das seções:

```txt
CPU
GPU NVIDEA
```

### Motivo

Destacar melhor os blocos principais da janela sem alterar as cores funcionais dos sensores e alertas.

### Testes

Validar sintaxe com `py_compile`.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-03 v01.16.py
```

## 2026-06-04 - v02.01 - Padronização dos tamanhos de fonte

### Ocorrido

Foi solicitado padronizar o tamanho das letras das informações numéricas dentro dos quadrados.

Também foi solicitado aumentar em 100% o tamanho dos títulos:

```txt
CPU
GPU NVIDEA
```

### Decisão

Usar nas informações numéricas dos quadrados o mesmo tamanho da segunda linha da GPU:

```txt
15
```

Alterar os títulos de seção de:

```txt
8
```

para:

```txt
16
```

### Motivo

Deixar as informações numéricas visualmente padronizadas e tornar os títulos das seções mais evidentes.

### Testes

Validar sintaxe com `py_compile` e leitura mínima de CPU/GPU.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-04 v02.00.py
```

## 2026-06-04 - v02.02 - Estados da CPU dentro do retângulo

### Ocorrido

Foi solicitado alterar o formato das informações da CPU que estavam fora da área de exibição em retângulo.

### Decisão

Mover os estados:

```txt
Estrangulamento térmico
Limite de potência
```

para dentro do retângulo da CPU.

A primeira linha da CPU mantém as três temperaturas.

A segunda linha da CPU passa a exibir duas colunas, cada uma com:

```txt
Título
Resultado
```

### Motivo

Deixar o bloco da CPU com o mesmo padrão visual do bloco `GPU NVIDEA`, mantendo as informações relacionadas dentro da mesma área de exibição.

### Testes

Validar sintaxe com `py_compile` e leitura mínima de CPU/GPU.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-04 v02.01.py
```

## 2026-06-04 - v02.03 - Rodapé de atualização em azul neon

### Ocorrido

Foi observado que a informação:

```txt
Atualizado a cada 2 segundos
```

ficou pouco visível após as mudanças de layout.

### Decisão

Manter a fonte original do rodapé:

```txt
Segoe UI 8
```

e alterar sua cor para azul neon.

Também foi aumentada apenas a altura da janela:

```txt
330x390 -> 330x430
```

### Motivo

Melhorar a leitura vertical e recuperar a visibilidade da informação de atualização sem alterar o tamanho horizontal da janela.

### Testes

Validar sintaxe com `py_compile` e leitura mínima de CPU/GPU.

### Como reverter

Voltar para a versão:

```txt
monitor-temperatura - 2026-06-04 v02.02.py
```

## 2026-06-04 - v02.04 - README atualizado para uso do zero

### Ocorrido

Foi solicitado atualizar o `README.md` para que uma pessoa com pouca ou nenhuma experiência em Python, Windows e instalação de aplicativos consiga preparar o ambiente e executar o monitor.

### Decisão

Reescrever o `README.md` com instruções simples e diretas cobrindo:

```txt
Instalação do Python
Instalação do HWiNFO
Configuração do log CSV
Execução do monitor pelo PowerShell
Leituras exibidas de CPU e GPU
Cores da interface
Versões usadas no projeto
Uso de IA, ChatGPT e Codex no desenvolvimento
```

### Arquivos alterados

```txt
README.md
DECISOES.md
```

O arquivo `monitor-temperatura.py` não foi alterado nesta versão.

### Motivo

O `README.md` anterior ainda descrevia o projeto como monitor apenas de CPU e não explicava o uso atual do HWiNFO CSV para CPU e GPU.

### Testes

Validar por leitura se o `README.md` informa:

```txt
Caminho do projeto
Caminho do CSV do HWiNFO
Comando de execução
Instalação do Python
Instalação do HWiNFO
```

### Como reverter

Voltar para o backup:

```txt
README - 2026-06-04 v02.03.md
```

## 2026-06-04 - v02.05 - Correção de acentuação do README

### Ocorrido

Foi observado que algumas palavras do `README.md` estavam sem a grafia correta do português do Brasil.

Exemplos informados:

```txt
visivel
maximo
termico
```

### Decisão

Corrigir a acentuação apenas no texto normal do `README.md`.

Os blocos de código, comandos, caminhos e nomes técnicos foram preservados.

### Arquivos alterados

```txt
README.md
DECISOES.md
```

### Motivo

Melhorar a qualidade da documentação sem alterar comandos ou trechos que precisam continuar exatamente como devem ser executados.

### Testes

Foi feita busca textual por palavras comuns sem acentuação após a correção.

### Como reverter

Voltar para o backup:

```txt
README - 2026-06-04 v02.04.md
```

## 2026-06-04 - v02.06 - Tratamento automático do JSON de limites

### Ocorrido

Foi definido que o arquivo `config-temperatura.json` deve ser o padrão usado pelo usuário para alterar limites de alerta sem mexer no arquivo Python.

### Decisão

Alterar o `monitor-temperatura.py` para ler e validar o JSON sempre que o app for aberto.

### Regras implementadas

Se o JSON não existir:

```txt
Criar o arquivo completo com os valores padrão.
```

Se o JSON existir, mas estiver totalmente inválido:

```txt
Recriar o arquivo completo com os valores padrão.
```

Se o JSON existir, mas estiver parcialmente inválido:

```txt
Manter os valores válidos do usuário.
Corrigir apenas as partes inválidas com os valores padrão.
Salvar novamente o JSON corrigido.
```

### Validação aplicada

Cada bloco de limite precisa ter:

```txt
amarelo
vermelho
```

Os valores precisam ser numéricos, entre `0` e `130`, e o limite amarelo precisa ser menor que o limite vermelho.

### Arquivos alterados

```txt
monitor-temperatura.py
config-temperatura.json
README.md
DECISOES.md
```

### Motivo

Permitir que o usuário edite limites de temperatura sem alterar o Python, mantendo o arquivo JSON funcional mesmo quando for apagado ou editado incorretamente.

### Testes

Validar:

```txt
JSON ausente
JSON totalmente inválido
JSON parcialmente inválido
JSON válido com valores personalizados
py_compile do Python
Leitura mínima de CPU/GPU
```

### Como reverter

Voltar para:

```txt
monitor-temperatura - 2026-06-04 v02.03.py
README - 2026-06-04 v02.05.md
config-temperatura - 2026-06-04 v02.05.json
```

## 2026-06-04 - v02.07 - Limite visual para uso da GPU

### Ocorrido

Foi questionado por que não existia um teste para o campo `Uso da GPU`.

### Decisão

Adicionar ao `config-temperatura.json` o bloco:

```txt
gpu_uso
```

com limites:

```txt
amarelo
vermelho
```

O campo `Uso da GPU` passa a usar as mesmas cores de alerta dos demais campos:

```txt
Verde neon
Amarelo
Vermelho piscando
```

### Validação aplicada

Como `Uso da GPU` é porcentagem, os valores válidos ficam entre:

```txt
0 e 100
```

O valor amarelo precisa ser menor que o valor vermelho.

### Arquivos alterados

```txt
monitor-temperatura.py
config-temperatura.json
README.md
DECISOES.md
```

### Motivo

Permitir que o usuário também configure alerta visual para uso alto da GPU sem alterar o arquivo Python.

### Testes

Validar:

```txt
py_compile do Python
JSON válido
Preservação dos valores personalizados existentes
Correção automática quando gpu_uso estiver inválido
Leitura mínima de CPU/GPU
```

### Como reverter

Voltar para:

```txt
monitor-temperatura - 2026-06-04 v02.06.py
README - 2026-06-04 v02.06.md
config-temperatura - 2026-06-04 v02.06.json
```
