class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances

    @lances.setter
    def lances(self, lance):
        self.__lances.append(lance)

