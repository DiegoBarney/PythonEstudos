import random

def jogo_advinha():
    print("*****************************")
    print("Bem vindo ao jogo de adivinha")
    print("*****************************")

    tentativas = 0
    numero_usuario = 0
    numero_aleatorio = 0


    #while((tentativas < 3) & (numeroUsuario != 10) ):
    for tentativas in range(1, 4):

        numero_aleatorio = random.randrange(0, 100)

        numero_usuario = input("Digite seu numero entre 1 e 100: ")

        print("Numero do usuario = ", numero_usuario)

        try:
            numero_usuario = int(numero_usuario)
        
            if(numero_usuario < 0 or numero_usuario > 100):
                raise Exception("Numero fora do padrao")

            if(numero_usuario == numero_aleatorio):
                print("Voce Acertou")
                break
            else:
                if(numero_usuario > numero_aleatorio):
                    print("Voce Errou, chutou um numero maior")
                if(numero_usuario < numero_aleatorio):
                    print("Voce Errou, chutou um numero menor")


        except Exception as Err:
            print("Ops...", Err)

def somar(a, b):
    return a + b;
      

if (__name__ == "__main__"):
    jogo_advinha()

