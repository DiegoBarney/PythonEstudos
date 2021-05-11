class Programa():

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano  
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        
    def __str__(self):
        return "Nome: {0} \nAno = {1}".format(self._nome, self._ano)



