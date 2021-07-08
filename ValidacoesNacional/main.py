import Documento as Documento
from buscaEndereco import buscaEndereco
import requests

end = buscaEndereco("13318000")
bairro, cidade, estado = end.retorna_dados_adicionais()

print(bairro, cidade, estado)
