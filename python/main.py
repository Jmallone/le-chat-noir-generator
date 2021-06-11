import bs4
import os
import re
import neocities
from senha import senha
nc = neocities.NeoCities(api_key=senha)

def find(nome):
    return soup.findAll("div",{"id":nome})

def change(el, text = '', tipo = 'normal', label = '', arq = ''):
    global soup

    if tipo == "block":
        content = change_block(arq)
        for c in content:
            nextLine = toMarkDown(c, el[0], content)
            if nextLine != 1:
                br = soup.new_tag("br")
                el[0].append(br)
        return 
        
    if tipo == "link":
        text = soup.new_tag("a", href=text)
        text.string = label

    for i in el:
        i.replace_with(text)

def sub(elemento, texto = '', tipo = 'normal', label = '', arq = ''):
    elementos = find(elemento)
    change(elementos, texto, tipo, label, arq)

def change_block(arq):
    return arq.read().split('\n')

def toMarkDown(texto, elemento, content):
    
    if texto != "" and (texto[0] == '[' or texto[0] == "!") and texto[-1] == ")":
        ''' Para Links com Frases Grandes ''' 
        palavras = []
        palavras.append(texto)
    else:
        ''' O restante do conteudo '''
        palavras = texto.split(" ")

    if palavras == ['']:
        return 

    for p in palavras:
        if p == '':
            ''' DOIS ESPAÇOS '''
            markup = "&nbsp;"
            s = bs4.BeautifulSoup(markup)
            elemento.append(s)
            continue 
    
        '''
            FORMATACAO DO TEXTO
        '''
        if p[0] == "*":

            if p[1] == "*":
                ''' Negrito '''
                tmp = fraseMarcacao(palavras,p, "*")
                criaTag(elemento, "b", tmp)
                
                pass
            else:
                ''' Italico '''
                tmp = fraseMarcacao(palavras,p, "*")
                criaTag(elemento, "i", tmp)
                pass        

        elif p[0] == "#":
            tmp = fraseMarcacao(palavras,p, "#")
            if p[1]=="#" and p[2] != "#":
                ''' h2 '''
                criaTag(elemento, "h2", tmp)
            elif p[2] == "#":
                ''' h3 '''
                criaTag(elemento, "h3", tmp)
            else:
                ''' h1 '''
                tmp = fraseMarcacao(palavras,p, "#")
                criaTag(elemento, "h1", tmp)

            return 1 

        elif p[-1] == ")" and (p[0]=="[" or p[0]=="!"):
            ''' LINKS '''

            label = re.findall(r"\[.+\]", p)[0].replace("[", "").replace("]", "")    
            link = re.findall(r"\(.+\)", p)[0].replace("(", "").replace(")", "")

            if p[0] == "!":
                ''' ACHOU UM LINK IMAGEM '''
                attr = {"src": link}
                criaTag(elemento, "img", "", attr)

            elif p[0] == "[":
                ''' ACHOU UM LINK'''
                attr = {"href": link}
                criaTag(elemento, "a", label, attr)

        elif p[0] == "~":
            ''' TAXADO '''
            tmp = fraseMarcacao(palavras,p, "~")
            criaTag(elemento, "s", tmp)
        
        elif p == "!---":
            ''' HR '''
            criaTag(elemento, "hr", "")

        elif p == "```":
            ''' Bloco Codigo '''
            bloco_codigo =  blocoMarcacao(content, p , "```")
            escreveBloco(elemento, bloco_codigo)

        elif p[0] == "`":
            tmp = fraseMarcacao(palavras,p, "`")
            attr = {"class": "codigo_single"}
            criaTag(elemento, "span", tmp, attr)

        elif p[0] == "¬":
            tab = "&nbsp;&nbsp;&nbsp; > "
            s = bs4.BeautifulSoup(tab)
            elemento.append(s)

        else:
            ''' Texto normal '''
            elemento.append(p+" ")
   
    return 
def escreveBloco(elemento, bloco_codigo):
    '''
        Pega o bloco e monta nas tags html correspondentes
    '''
    numero_linhas = len(bloco_codigo)
    attr = {"class": "code"}
    table  = criaTag(elemento, "table", "", attr)

    attr = {"class": "numero"}
    td_numero = criaTag(table, "td", "", attr)

    attr = {"class": "container"}
    td_container = criaTag(table, "td", "", attr)

    for i in range(numero_linhas):
        attr = {"class": "linha"}
        criaTag(td_numero, "div", str(i+1), attr)

    for i in bloco_codigo:
        attr = {"class": "codigo"}
        criaTag(td_container, "div", i, attr)

def blocoMarcacao(content, p, marca):
    '''
            ira pegar os blocos de codigo
            ``` 
            Linha 1
            Linha 2
            linha 3
            ```
            retirar eles de content 
            -----------
            retorn ['Linha1', 'Linha2', 'Linha3']
    '''
    inicio = content.index(p)
    fim = -1

    for i in content[inicio+1:]:
        if i == marca and fim == -1:
            fim = content[inicio+1:].index(i)
    fim =  inicio+fim

    tmp = content[inicio+1:fim+1]
    del content[inicio-1:fim+1]

    return tmp
def fraseMarcacao(palavras,p, marca):
    '''
        palavras = ['Oi', '~~Aqui','esta', 'taxado~~', 'fim!']
        retira o ~~Aqui esta taxado~ da palavras
        -------------------------------
        return "Aqui esta taxado"
    '''
    
    ''' Retorna frases que contem o h1 h2 ou h3'''
    if p[0] == "#":
        return " ".join(palavras).replace("#", "")

    comeco = -1
    fim = -1

    #TODO As vezes se vier o final '' buga por isso tira logo ele 
    if palavras[-1] == '':
        del palavras[-1]
    
    for i in palavras:
        if i[-1] == marca and fim == -1:
            fim = palavras.index(i)

    comeco = palavras.index(p)

    ''' ~~Pega Frases Longas e retira da Lista `Palavras` '''
    tmp = " ".join(palavras[comeco:fim+1]).replace(marca, "")
    
    if comeco == fim:
        '''
        se não colocar o " ", 
        o P vai pro proximo elemento quando tem 2 tags na mesma frase
        '''
        del palavras[comeco]
        palavras.insert(0," ")
    else:
        del palavras[comeco:fim]

    return tmp


def criaTag(elemento, tag_name, label, attr={}):

    '''
        Cria um tag do tipo TAG_NAME
        e adiciona um espaco na frente dessa nova tag
        ---------------
        return tag_criada
    '''
    tag = soup.new_tag(tag_name, attrs=attr)
    tag.string = label
    elemento.append(tag)
    elemento.append(" ")
    return tag

def montaHeader():
    '''
            Name and Menu bar
    '''
    header_f = open("textos/header.txt", "r")

    titulo = header_f.readline().replace("\n","")
    home =  header_f.readline().replace("\n","")
    twitter = header_f.readline().replace("\n","")
    github = header_f.readline().replace("\n","")

    sub("titulo", titulo)
    sub("home_link", home, "link", "home")
    sub("twitter_link", twitter, "link", "twitter")
    sub("github_link", github, "link", "github")

    header_f.close()

def montaPagina(paginas):
   global soup 
   with open("../site/index.html") as info:
        txt = info.read()
        soup_index = bs4.BeautifulSoup(txt)

   for p in paginas:
        with open("template/template-post.html") as inf:
            txt = inf.read()
            soup = bs4.BeautifulSoup(txt)

        post_f = open(f"textos/pages/{p}.txt")
        titulo = post_f.readline().replace("\n","")
        date = post_f.readline().replace("\n","")
        sub("conteudo",tipo="block", arq=post_f)
        sub("titulo-post", titulo)
        sub("date", date)
        montaHeader()


        br = soup.new_tag("br")
        a_tag = soup_index.new_tag("a", href=f"pages/{p}.html")
        a_tag.string = f">>> {titulo} - {date}"
        i = soup_index.find("div",{"id":"allPosts"})
        i.append(a_tag)
        i.append(br)

        with open("../site/index.html", "w") as outf:
            outf.write(str(soup_index))

        with open(f"../site/pages/{p}.html", "w") as outf:
            outf.write(str(soup))



global soup
with open("template/template-index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt)

'''
        Name and Menu bar
'''
montaHeader()
'''
        Who i'am
'''
about_f = open("textos/about.txt", 'r')
sub("about",tipo="block", arq=about_f)

about_f = open("textos/about-2.txt", 'r')
sub("about-2",tipo="block", arq=about_f)

about_f.close()


# save the file again
with open("../site/index.html", "w") as outf:
    outf.write(str(soup))

'''
    Posts
'''

basepath = 'textos/pages/'
paginas = []
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        paginas.append(entry.split(".txt")[0])

montaPagina(paginas)

nc.upload(('../site/index.html', 'index.html'))

print("\n\n\n\n\n\n\n\n\n\n\n")
le_chat = ("""
_._     _,-'""`-._
(,-.`._,'(       |\`-/|     Le Chat Noir
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
""")

print(le_chat)
print("\n\n -------------------Uploading Posts:\n")

for p in paginas:
    nc.upload((f"../site/pages/{p}.html", f"/pages/{p}.html"))
    print(f"Uploading... {p}")
# curl -H "Authorization: Bearer API_KEY" https://neocities.org/api/list?path=pages

'''
    Uploading estilo.css
'''
nc.upload((f"../site/estilo.css", f"/estilo.css"))
print("-- Uploading estilo.css")

print("\n")
