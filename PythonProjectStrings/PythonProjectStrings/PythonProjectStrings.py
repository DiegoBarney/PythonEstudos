from Extrator import ExtratorArgumentoURL
from Padrao import PadroesUtils

url = "google.com.br"
telefone = "meu telefone é 96485-5252, favor ligar no horario comercial"



PadroesUtils.encontra_telefone(telefone)
print(ExtratorArgumentoURL.string_eh_valida(url))