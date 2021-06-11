# Le Chat Noir Generator :cat:
Gerador de Páginas Estaticas para o [Neocities](hhtp://neocities.org/).

## Depedências

```bash
pip install neocities
pip install beautifulsoup4
```

## Como usar

Para fazer upload no Neocities gere um API_KEY através do site `https://neocities.org/api` e crie um arquivo na pasta `python/` chamado `senha.py` com o seguinte conteudo:

```python
# python\senha.py
senha = "SUA_API_KEY_AKI"
```

* * *
### Criando um post
Todo arquivo `.txt` dentro da pasta `python\textos\pages` será transformado em uma postagem e linkado no `index.html`.

Os arquivos `.txt` deve possuir a seguinte ordem:
```
Primeira Linha: O Titulo
Segunda Linha: A data
A proximas Linhas: O Corpo do post
```

Exemplo:
`python\textos\ola.txt`
```
Olá Pessoal :)
08/06/2021
Este é um post exemplo,
Muito obrigado por ler.
Aproveite 
```

* * *

### Upload para o Site
Para fazer o upload das paginas geradas execute o arquivo `python\main.py`

``` bash
python main.py
```

## Características
Le chat noir possui suporte para algumas tags em Markdown, sendo elas:

| Nome             | Comando                                              |
|------------------|------------------------------------------------------|
| *Italico*        | `*italico*`                                          |
| **Negrito**      | `**Negrito**`                                        |
| ~~Taxado~~       | `~~Taxado~~`                                         |
| Barra Vertical   | `!---`                                               |
| `Codigo Simples` | \`Codigo Simples\`                                   |
| ``Codigo Simples``| \`\`\`Codigo Simples\`\`\`                          |
| Imagem           | `![gatinho](https://neocities.org/img/heartcat.png)` |
| Link             | `[google](https://www.google.com.br)`                |
| H1               | `# Texto aqui h1`                                    |
| H2               | `## Texto aqui h2`                                   |
| H3               | `### Texto aqui h3`                                  |

Novas tags em breve!

## Video Demo
https://user-images.githubusercontent.com/6977257/121244485-4cca7e80-c875-11eb-947f-66f62ea64597.mp4
