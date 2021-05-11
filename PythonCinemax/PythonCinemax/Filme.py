import Programa

class Filme(Programa.Programa):

    def __init__(self, nome, ano, duracao ):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
          return super().__str__()+" \nDuracao = {0}\n".format(self.duracao)

   


