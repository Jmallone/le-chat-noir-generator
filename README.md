# Le Chat Noir Generator
Gerenciador de Páginas Estaticas para o [Neocities](hhtp://neocities.org/).

## Depedências
> pip install neocities

> pip install beautifulsoup4

## Como usar

Para fazer upload no Neocities gere um API_KEY através do site `https://neocities.org/api` e crie um arquivo na pasta `python/` chamado `senha.py` com o seguinte conteudo:

`python\senha.py`
> senha = "SUA_API_KEY_AKI"

* * *
Todo arquivo `.txt` dentro da pasta `python\textos\pages` será transformado em uma postagem e linkado no `index.hmtl`.

Os arquivos `.txt` deve possuir a seguinte ordem:
```
Primeira linha o Titulo
Segunda Linha: A data
A proximas Linhas o Corpo do post
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
Para fazer o upload do site use o execute o arquivo `main.py`
> python python/main.py

## Características
Le chat noir possui suporte para algumas tag em Markdown para ser usada no corpo dos posts entre elas:

*italico* `*italico*`

**negrito** `**negrito**`

# h1 `#h1`

## h2 `##h2`

### h3 `###h3`

Novas tag em breve!

## Video Demo
https://github.com/Jmallone/le-chat-noir-generator/blob/master/video.mp4
