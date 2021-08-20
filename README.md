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
### Editando o Menu
Para editar o menu modifique o arquivo `python\textos\header.txt`
O arquivo `header.txt` deve seguir a ordem:
```
Primeira Linha: Titulo do Site
As proximas Linhas: label_do_link link
```

Exemplo:
`python\textos\header.txt`
```
JMallone's Page
home https://jmallone.neocities.org/index.html
twitter https://twitter.com/jmallone2
github https://github.com/Jmallone
twitch https://www.twitch.tv/jmallone01
```

NOTA: entre a `label_do_link` e o `link` tem que haver um espaço.

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
| > Tabulacao com >| `¬ Tabulacao com >`                                  |
| `Codigo Simples` | \`Codigo Simples\`                                   |
| ``Bloco Codigo`` | \`\`\`Bloco Codigo\`\`\`                             |
| Imagem           | `![gatinho](https://neocities.org/img/heartcat.png)` |
| Imagem Centralizada        | `!c[gatinho](https://neocities.org/img/heartcat.png)` |
| Imagem Centralizada e Redimensiona a imagem em 90% | `!c/90[gatinho](https://neocities.org/img/heartcat.png)` |
| Link             | `[google](https://www.google.com.br)`                |
| H1               | `# Texto aqui h1`                                    |
| H2               | `## Texto aqui h2`                                   |
| H3               | `### Texto aqui h3`                                  |

Novas tags em breve!

## Video Demo
https://user-images.githubusercontent.com/6977257/121244485-4cca7e80-c875-11eb-947f-66f62ea64597.mp4
