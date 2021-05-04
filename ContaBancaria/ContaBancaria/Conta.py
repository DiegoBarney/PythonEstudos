
class Conta:

    def __init__(self, conta, agencia, saldo, titular):
        self.__conta = conta
        self.__agencia = agencia
        self.__saldo = saldo
        self.__titular = titular


    def sacar(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
  

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def transferir(self, contaDestino, valor):
        if valor < self.__saldo:
            self.sacar(valor)
            contaDestino.depositar(valor)

    def extrato_conta(self):
        print("Titular = {0}, Conta = {1}, Agencia = {2}, Saldo = {3}".format(self.__titular, self.__conta, self.__agencia, self.__saldo))

   