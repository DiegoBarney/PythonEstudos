class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    def propoe(self, lance):
        self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]



