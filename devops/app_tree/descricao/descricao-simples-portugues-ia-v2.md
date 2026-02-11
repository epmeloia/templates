# Descrição Simples em Portugues IA
"descricao-simples-portugues-ia.md"

---
## APP:
- Sua Função é de Registro de Textos, com Imagens e links.
- Será uma aplicação WEB.
- Quando o APP é aberto, seu Banco de Dados está em sem dados em branco, neste momento o sistema está em estado de inicio, todas as suas configurações são as do PADRÃO.

---
## Banco de Dados:
- Será Armazenado em  Drive Virtual, para compartilhamento entre Plataformas.
- Banco de Dados: Botão para Abrir Banco de Dados, ao ser carregado, são atualizados todos as informaçãoes de Pastas (janela da Esquerda) e Descricão (Janela da Esquerda), e tambem todos os padrões: Fonte, Tamanho da Fonte, Tema.
- Banco de Dados: Botão para Salvar Banco de Dados, guarda todos os dados digitados no APP até o momento, como tambem o Padrão que está em uso no APP, de Fonte/Tamanho/Tema.

---

## Configurações PADRÃO:

### Geral:
- Abertura do APP, o Banco de Dados não tem dados, está em branco;
- Tema Claro do Sistema;
- Fonte da Área de Descrição é Lucida Console;
- Tamanho da Fonte da Área de Descrição 14px;
- Cor da Fonte da Área de Descrição Preta (para Tema Claro);
- Alinhamento da Área de Descrição Esquerdo;
- Fundo da Área de Descrição em Branco (para Tema Claro);
- Tecla "ENTER" é usada nos PopUps sempre para "Confirmar" a Ação;
- Tecla "ENTER" do Teclado Numérico é usada nos PopUps sempre para "Confirmar" a Ação;
- Tecla "ESC" é usada nos PopUps sempre para "Cancelar" a Ação;
- No Popup de Criação de Pasta Tipo "Raiz", dentro do Campo Nome da Raiz, o cursor do teclado deve estar na primeira posição do Campo;
- No Popup de Criação de Pasta Tipo "SubPasta", dentro do Campo Nome da Raiz, o cursor do teclado deve estar na primeira posição do Campo;


### TEXTO:
- Texto > Fonte: Padrao Inicial "Lucida Consele".
- Texto > Fonte > Evolução: Seleção Via ComboBox, outras a serem incluidas: Arial, Tahoma, Times New Roma, Outras.
- Texto > Fonte: Ao ser selecionado uma nova fonte, ela se torna padrão para o sistema inteiro, todos os textos que já estão no APP e que forem digitados apartir deste momento, utilizam essa fonte.
- Texto > Tamanho: Padrao Inicial "14px".
- Texto > Tamanho: Evolução: Seleção Via ComboBox, outras a serem incluidas: 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 30.
- Texto > Área de Descrição > Alinhamento: Padrao Inicial "Direita"
- Texto > Área de Descrição > Alinhamento: Seleção via ComboBox: Direita, Esquerda, Centralizada, Justificada (similar ao comportamento do Notepad++).
- Texto > Área de Descrição > Limite Vertical: Não existe limite (similar ao comportamento do  Word).
- Texto > Área de Descrição > Alinhamento: Ao deslocar o cursor do mouse sobre o texto, oa informação no "ComboBox" é atualizada em tempo real (similar ao comportamento do  Word).
- Texto > Área de Descrição > Formatação: ao se digitar uma paravla, no momento da digitação ultrapassa ou ir até a borda direita limitadora noi limite da tela, a palavra inteira deve ser realocada para a próxima linha dinâmicamente (similar ao comportamento do Notepad++)


### IMAGEM:
- Imagem > Área de Descrição > Ao ser colada uma Imagem, ele fica em um parágrafo unico e separada do Texto (similar ao comportamento do  Word).
- Imagem > Edição: Apenas a alteração de Tamanho é permitida, a qualquer momento (similar ao comportamento do  Word).
- Imagem > Seleção: Pode ser selecionada para ser Copiada ou/e Recortada, e utilizada novamente no mesmo texto ou em outro texto  (similar ao comportamento do  Word).


### PASTAS:
- Pastas > Raiz > Criação: Botão para criação exclusiva de Pasta Raiz.
- Pastas > Raiz > Criação: Utiliza de combobox para "Criar Raiz" ou "Cancelar".
- Pastas > Raiz > Exclusão > COM SUBPASTAS: Permitido mas com PopUp, informando que Existe SUBPASTAS e que serão Excluidas Junto com a Raiz, e movimentadas para a Pasta de DELETADOS.
- Pastas > Raiz > Exclusão > SEM SUBPASTAS: Abrir um PopUp solicitando a "Exclusão" ou "Cancelamento".
- Pastas > Raiz > Exclusão > SEM SUBPASTAS > Cancelamento: Esta ação deixa a Pasta do Tipo Raiz e seus dependentes, bem como os dados de Descrição sem alteração nenhuma.
- Pastas > Raiz > Exclusão > SEM SUBPASTAS > Exclusão: Esta ação faz com que a Pasta do Tipo Raiz e todas as SubPastas dependentes desta Pasta do Tipo Raiz como tambem todas as Descrições, sejam movidas para a Pasta Especial "DELETADOS", sua estrutura deve ser totalmente preservada, da Raiz e Subpastas e Descrições.
- Pastas > Pasta de DELETADOS > Pasta RAIZ: Ao ser colocada na Pasta Especial DELETADOS, é colocada a sua direita somente Dois Ícones, um representando uma "Exclusão DEFINITIVA" e outro para a "RECUPERAÇÃO".
- Pastas > Pasta de DELETADOS > Pasta RAIZ > EXCLUSÃO DEFINITIVA: Abrir PopUp solicitando a Confirmação ou Cancelamento da opção.
- Pastas > Pasta de DELETADOS > Pasta RAIZ > EXCLUSÃO DEFINITIVA > PopUp Confirmação: Ação provoca a Exclusão definitiva da pasta e das "SubPastas" dependentes, como tambem dos dados de "Descrição" de todas delas.
- Pastas > Pasta de DELETADOS > Pasta RAIZ > EXCLUSÃO DEFINITIVA > PopUp Cancelamento: Esta ação deixa a Pasta do Tipo Raiz e seus dependentes, bem como os dados de Descrição sem alteração nenhuma.
- Pastas > Pasta de DELETADOS > Pasta RAIZ > Ícone de RECUPERAÇÃO: Abrir PopUp solicitando a Confirmação ou Cancelamento da opção.
- Pastas > Pasta de DELETADOS > Pasta RAIZ > Ícone de RECUPERAÇÃO > PopUp Confirmação: Ação provoca a Restauração definitiva da pasta e das "SubPastas" dependentes, como tambem dos dados de "Descrição" de todas delas.
- Pastas > Pasta de DELETADOS > Pasta RAIZ > Ícone de RECUPERAÇÃO > PopUp Cancelamento: Esta ação deixa a Pasta do Tipo Raiz e seus dependentes, bem como os dados de Descrição sem alteração nenhuma.
- Pastas > Pasta de DELETADOS > Pasta SUBPASTAS: recebe a sua Direita apenas Dois Ícones: Um para Exclusão DEFINITIVA e outro para a RECUPERAÇÃO.


## Vou desenvolver um app web, para controle de Idéias e Informações, ele utiliza de um formato similar ao explorer, com Pastas na parte esquerda da tela e o selecionar uma delas abre na parte direita da tela opção de entrar com um texto, podendo ser importados texto esternos, que serão convertidos para a fonte e formato padrão que é a esquerda, algo como copiar um texto de word para dentro do notepad++, podem ser colocadas imagens, que devem ter a possibilidade de alteração de tamanho, com relação a fonte do texto o padrão inicial e "Lucida Console", mas deve ser possivel alterar para mais umas 5 fontes (Arial | Tahoma | Times New | etc), essa fonte quando alterada é padrão para todos os textos a serem colocados ou já colocados no app, a cor da fonte é sempre preta, o alinhamento dos parágrafos por padrão é a esquerda mas pode ser alterado (Direita|Central|Justificado), os limites das bordas da tela direita e esquerda são limitantes para os textos e a quando acontece de uma palavra esbarrar na borda ele deve ser colocada inteira na próxima linha, 

 
##----------####----------####----------####----------##
