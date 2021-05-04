
class Conta:

    def __init__(self, conta, agencia, saldo, titular, limite = 200):
        self.__conta = conta
        self.__agencia = agencia
        self.__saldo = saldo
        self.__titular = titular
        self.__limite = limite
   

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
        print("Titular = {0}, Conta = {1}, Agencia = {2}, Saldo = {3}, limite = {4}".format(self.__titular, self.__conta, self.__agencia, self.__saldo, self.__limite))

    def get_saldo(self):
        return self.__saldo

    def get_agencia(self):
        return self.__agencia


    def get_titular(self):
        return self.__titular

    def get_conta(self):
        return self.__conta

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novoLimite):
        if novoLimite < 0:
            raise Exception("Limite não pode ser menor que 0")
        else:
            self.__limite = novoLimite