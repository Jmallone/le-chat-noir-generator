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
        #el.append("<br>")
        for c in content:
            nextLine = toMarkDown(c, el[0])
            if nextLine != 1:
                br = soup.new_tag("br")
                el[0].append(br)
        return 
        
    if tipo == "link":
        #text = "<a href='"+text+"'>"+label+"</a>"
        
        #criaTag(elemento, tag_name, label):
        text = soup.new_tag("a", href=text)
        text.string = label
        #print(text)

	#<a href="<p id='home_link'></p>">home</a>&nbsp;
    for i in el:
        i.replace_with(text)

def sub(elemento, texto = '', tipo = 'normal', label = '', arq = ''):
    elementos = find(elemento)
    change(elementos, texto, tipo, label, arq)

def change_block(arq):
    return arq.read().split('\n')

def toMarkDown(texto, elemento):
    ''' FIX: Quando tem 2 espaços tem que manter um'''
    palavras = texto.split(" ")
    if palavras == ['']:
        return 

    for p in palavras:
        if p == '':
            return 
    
        '''
            FORMATACAO DO TEXTO
        '''
        if p[0] == "*" and p[-1] == "*":
            tmp = p.replace("*","")
            if p[1] == "*":
                ''' Negrito '''
                criaTag(elemento, "b", tmp)
                pass
            else:
                ''' Italico '''
                criaTag(elemento, "i", tmp)
                pass        

        elif p[0] == "#":
            tmp = p.replace("#", "")
            if p[1]=="#" and p[2] != "#":
                ''' h2 '''
                criaTag(elemento, "h2", tmp)
            elif p[2] == "#":
                ''' h3 '''
                criaTag(elemento, "h3", tmp)
            else:
                ''' h1 '''
                criaTag(elemento, "h1", tmp)
            return 1 
        #elif p[0] == "!" and p[1] == "[":
        elif p[-1] == ")" and (p[0]=="[" or p[0]=="!"):
            ''' LINKS '''
            label = re.findall(r"\[\w+\]", p)[0].replace("[", "").replace("]", "")    
            link = re.findall(r"\(.+\)", p)[0].replace("(", "").replace(")", "")
            #label = re.findall(r"\[\w+\]", p)    
            #print(label)
            #print(p)
            if p[0] == "!":
                ''' ACHOU UM LINK IMAGEM '''
                #criaTag(elemento, "b", "Achei uma imagem")
                tag = soup.new_tag("img", src=link)
                #tag.string = label+" "

            elif p[0] == "[":
                ''' ACHOU UM LINK'''
                #criaTag(elemento, "b", "Achei um Link")
                tag = soup.new_tag("a", href=link)
                tag.string = label
            elemento.append(tag)
            elemento.append(" ")

                
        else:
            ''' Texto normal '''
            elemento.append(p+" ")
   
    return 

#TODO criar um tipo link aqui
def criaTag(elemento, tag_name, label):

    #tag = soup.new_tag(tag_name, href=text)
    #tag.string = label

    tag = soup.new_tag(tag_name)
    tag.string = label+" "
    elemento.append(tag)

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

print("\n\n")
