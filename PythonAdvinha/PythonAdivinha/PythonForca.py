import random

def jogo_forca():

    imprime_intro_jogo()

    palavra_forca = gerar_palavra_aleatoria()


    acertou = False
    enforcou = False
    index = 0
    forca = ["_" for palavra in palavra_forca]
    erros = 0

    while(not acertou and not enforcou):

        letra = input("Digite uma letra: ").lower()
        index = 0

        copia = forca.copy()

        for x in palavra_forca:
            
            if letra == x:
                forca[index] = letra

            index = index + 1
    

        if copia == forca:
            erros = erros +1
            desenha_forca(erros)

        if erros >= 7:
            imprime_mensagem_perdedor(palavra_forca)
            enforcou = True
            continue

        print("Forca: ", forca) 

        if not "_" in  forca:
            imprime_mensagem_vencedor()
            acertou = True



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

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogo_forca()     
               
         
