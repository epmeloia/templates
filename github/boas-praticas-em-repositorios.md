# Boas Práticas em Repositórios
"boas-praticas-em-repositorios.md"

---

## Tópicos
- [Pastas Estrutura e Organização:](#Pastas Estrutura e Organização:)
- [Nomes de Pastas e Arquivos:](#Nomes de Pastas e Arquivos:)
- [Títulos e Textos:](#Títulos e Textos:)
Arquivos Padrão e Metadados:


***

### Pastas Estrutura e Organização:

Uma estrutura de diretórios organizada ajuda outros desenvolvedores a entenderem o propósito e a hierarquia dos arquivos rapidamente :[1]

```
/src        → código-fonte principal
/tests      → testes automatizados
/docs       → documentação técnica
/scripts    → scripts auxiliares (build, deploy, migrações)
.github     → templates de issues, pull requests e configurações da comunidade
```

Outras pastas opcionais e comuns:
- **/assets** – imagens, ícones, vídeos e mídias usadas no projeto.  
- **/config** – arquivos de configuração (por exemplo, JSON ou YAML).  
- **/examples** – exemplos de uso do código ou pequenos projetos de demonstração.


***

### Nomes de Pastas e Arquivos:

As boas práticas seguem princípios de clareza e consistência :[2][1]
- Use **letras minúsculas** e **hifens (-)** no lugar de espaços (`meu-projeto`, `utils-scripts`).  
- Evite acentos, caracteres especiais ou letras maiúsculas em diretórios.  
- Prefira **nomes descritivos**: `image-processor.py` é melhor que `ip.py`.  
- Git não monitora pastas vazias, então adicione um arquivo `.gitkeep` para preservar diretórios vazios quando necessário.[3]


***

### Títulos e Textos:

Os arquivos `README.md`, `CONTRIBUTING.md` e similares usam **Markdown**. Os títulos devem seguir a hierarquia recomendada pelo GitHub :[4]
```
# Nível 1
## Nível 2
### Nível 3
```
  
O README é o “cartão de visita” do repositório e deve conter :[5][6]
- Nome do projeto  
- Descrição e propósito  
- Instruções de instalação e uso  
- Tecnologias utilizadas  
- Exemplos e capturas de tela  
- Licença e autoria  

O GitHub gera automaticamente um **índice navegável** baseado nos títulos do README.


***

### Arquivos Padrão e Metadados:

Use arquivos específicos para padronizar a comunidade do projeto :[7][8]
- `.gitignore` – define o que não será versionado.  
- `LICENSE` – descreve os direitos de uso do código.  
- `CONTRIBUTING.md` – guia de contribuição.  
- `CODE_OF_CONDUCT.md` – boas práticas para colaboradores.  
- Arquivos dentro de **`.github/`**, como templates de issues e PRs, são aplicados globalmente na organização.


***

### README - Representar a Estrutura:

Para exibir a árvore de diretórios em Markdown, pode-se gerar via comando `tree` :[9]
```
$ tree -a
```
Exemplo de saída formatada:
```
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── README.md
└── .gitignore
```

tree -a -L 2


***

Seguindo essas práticas, um repositório GitHub mantém **clareza, legibilidade e consistência**, facilitando colaboração e manutenção.

[1](https://www.dio.me/articles/boas-praticas-de-organizacao-para-repositorios-git-eficiencia-e-clareza-no-codigo-088d74f7d99e)
[2](https://docs.github.com/pt/repositories/working-with-files/managing-files/creating-new-files)
[3](https://pt.stackoverflow.com/questions/437043/como-criar-uma-pasta-dentro-do-meu-reposit%C3%B3rio-no-github)
[4](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
[5](https://www.alura.com.br/artigos/escrever-bom-readme)
[6](https://www.dio.me/articles/personalize-o-readme-no-github)
[7](https://docs.github.com/pt/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
[8](https://docs.github.com/pt/repositories/creating-and-managing-repositories/best-practices-for-repositories)
[9](https://agilso.com/6-como-representar-a-estrutura-de-diretorios-e-arquivos-em-texto-markdown)
[10](https://www.youtube.com/watch?v=PpVJ2HxpXAE)
[11](https://docs.github.com/pt/repositories/working-with-files/managing-files)
[12](https://github.com/JuniorLima22/padroes-e-nomenclaturas-no-git)
[13](https://www.reddit.com/r/github/comments/175lsoc/is_there_a_tool_that_creates_a_folder_structure/)
[14](https://github.com/iuricode/padroes-de-commits)
[15](https://www.youtube.com/watch?v=Xsulc8agj_A)
[16](https://github.com/frontendbr/forum/discussions/2407)
[17](https://www.reddit.com/r/programming/comments/gbe0rl/git_branch_naming_conventions/)
[18](https://www.youtube.com/watch?v=EGmzAs1G0z0)
[19](https://www.youtube.com/watch?v=oVnenyWTndY)
[20](https://docs.github.com/pt/get-started/start-your-journey/uploading-a-project-to-github)





##----------####----------####----------####----------##