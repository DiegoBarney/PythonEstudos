
def JogoForca(palavraForca):
    print("*****************************")
    print("Bem vindo ao jogo da forca")
    print("*****************************")

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


if (__name__ == "__main__"):
    JogoAdvinha()     
               
         
