class ExtratorArgumentoURL:
    def __init__(self,url):
        if self.string_eh_validaa(url):
            self.url = url
        else:
            raise LookupError("Url inválida")

    @staticmethod
    def string_eh_valida(url):
        if url:
            return True
        else:
            return False

    def retorna_moedas(self):
        busca_moeda_origem = "moedaorigem"
        busca_moeda_destino = "moedadestino"

        inicio_substring_moeda_origem = self.encontraIndiceInicioSubstring(busca_moeda_origem)
        final_substring_moeda_origem = self.url.find("&")
        moeda_origem = self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]

        inicio_substring_moeda_destino = self.encontraIndiceInicioSubstring(busca_moeda_destino)
        final_substring_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[inicio_substring_moeda_destino:]

        return moeda_origem, moeda_destino

    def encontra_indice_inicio_substring(self, moeda_ou_valor):
        return self.url.find(moeda_ou_valor) + len(moeda_ou_valor) + 1



