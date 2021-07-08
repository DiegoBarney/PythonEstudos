import requests

class buscaEndereco:
    def __init__(self, cep):

        if self.cep_eh_valido(cep):
            self.cep = str(cep)
        else:
            raise ValueError("Cep invalido")

    def cep_eh_valido(self, cep):
        if(len(cep) == 8):
            return True
        else:
            return False

    def __str__(self):
        return self.format_cep()

    def retorna_dados_adicionais(self):
        retorno = requests.get('https://viacep.com.br/ws/' + self.cep + '/json')
        return retorno.text

    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])