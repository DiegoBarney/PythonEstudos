import re

class PadroesUtils:

    @staticmethod
    def encontra_telefone(telefone):

        padrao_telefone = "[0-9]{5}-[0-9]{4}"

        retorno = re.search(padrao_telefone, telefone)

        print(retorno.group())