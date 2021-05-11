import Programa

class Serie(Programa.Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


    def __str__(self):
        return super().__str__()+" \nTemporadas = {0}\n".format(self.temporadas)


    


