import Documento as Documento
from buscaEndereco import buscaEndereco
import requests

end = buscaEndereco("13318000")
dados = end.retorna_dados_adicionais()

print(dados)
