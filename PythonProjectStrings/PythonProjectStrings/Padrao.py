import re

class PadroesUtils:

    @staticmethod
    def encontra_telefone(telefone):

        padrao_telefone = "[0-9]{4,5}[-]*[0-9]{4}"

        retorno = re.search(padrao_telefone, telefone)

        print(retorno.group())


    @staticmethod
    def encontra_telefones(telefone):
       
        padrao_telefone = "[0-9]{4,5}[-]*[0-9]{4}"

        retorno = re.findall(padrao_telefone, telefone)

        print(retorno)