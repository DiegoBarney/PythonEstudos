import random

def JogoAdvinha():
    print("*****************************")
    print("Bem vindo ao jogo de adivinha")
    print("*****************************")

    tentativas = 0
    numeroUsuario = 0
    numeroAleatorio = 0


    #while((tentativas < 3) & (numeroUsuario != 10) ):
    for tentativas in range(1, 4):

        numeroAleatorio = random.randrange(0, 100)

        numeroUsuario = input("Digite seu numero entre 1 e 100: ")

        print("Numero do usuario = ", numeroUsuario)

        try:
            numeroUsuario = int(numeroUsuario)
        
            if(numeroUsuario < 0 or numeroUsuario > 100):
                raise Exception("Numero fora do padrao")

            if(numeroUsuario == numeroAleatorio):
                print("Voce Acertou")
                break
            else:
                if(numeroUsuario > numeroAleatorio):
                    print("Voce Errou, chutou um numero maior")
                if(numeroUsuario < numeroAleatorio):
                    print("Voce Errou, chutou um numero menor")


        except Exception as Err:
            print("Ops...", Err)

def somar(a, b):
    return a + b;
      

if (__name__ == "__main__"):
    JogoAdvinha()

