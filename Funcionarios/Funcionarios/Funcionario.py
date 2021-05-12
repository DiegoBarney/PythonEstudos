from datetime import datetime

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.__marcacao_saida = 0
        self.__marcacao_entrada = 0

    def registra_horas_entrada(self):
        self.__marcacao_entrada = datetime.now()

    def registra_horas_saida(self):
        if self.__marcacao_entrada != datetime.now():
            self.__marcacao_saida = datetime.now()
        else:
            raise Exception("Não pode marcar dois pontos seguidos")

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


    @property
    def marcacao_entrada(self):
        return self.__marcacao_entrada.strftime("%d/%m/%Y %H:%M:%S")

    @property
    def marcacao_saida(self):
        return self.__marcacao_saida


