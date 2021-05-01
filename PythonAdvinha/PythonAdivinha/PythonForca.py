import random

def jogo_forca():

    imprime_intro_jogo()

    palavraForca = gerar_palavra_aleatoria()


    acertou = False
    enforcou = False
    index = 0
    forca = ["_" for palavra in palavraForca]
    erros = 0

    while(not acertou and not enforcou):

        letra = input("Digite uma letra: ").lower()
        index = 0

        copia = forca.copy()

        for x in palavraForca:
            
            if letra == x:
                palavraForca = palavraForca.replace(x,'0',5)
                forca[index] = letra

            index = index + 1
    

        if copia == forca:
            erros = erros +1

        if erros >= 5:
            print("voce perdeu!!")
            enforcou = True
            continue

        print("Forca: ", forca) 

        acertou = not "_" in  forca


def imprime_intro_jogo():
    print("*****************************")
    print("Bem vindo ao jogo da forca")
    print("*****************************")

def gravar_palavras_arquivo():
    arquivo = open("palavras.txt", "w")
    arquivo.write("manga\n");
    arquivo.write("pera\n");
    arquivo.write("uva\n");
    arquivo.write("jabuticaba\n");
    arquivo.close()

def capturar_palavras_arquivo():
    arquivo = open("palavras.txt", "r")

    palavras = arquivo.readlines()

    palavras_new = []

    for palavra in palavras:
        palavras_new.append(palavra.strip())

    arquivo.close()

    return palavras_new

def gerar_palavra_aleatoria():
    palavras_new = capturar_palavras_arquivo()
    posicao = random.randrange(0, len(palavras_new))
    return palavras_new[posicao]


if (__name__ == "__main__"):
    jogo_forca()     
               
         
