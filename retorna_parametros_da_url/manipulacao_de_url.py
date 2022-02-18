class manipulacao_de_url:

    def __init__(self, url):
        self.url = url

    def indice_interrogacao(self, url):
        indice_interrogacao = url.find('?')
        return indice_interrogacao

    def encontrar_parametros(self, indice_interrogacao, url):
        count = False
        lista = []
        conta = 0
        quantidade_de_ecomercial = url.count("&")

        while (conta<=quantidade_de_ecomercial-1):

            if (count == False):
                final = url.find('&')
                inicio = url.find('=')
                lista.append(url[indice_interrogacao+1:inicio])
                url = url[final: len(url)]
                count = True

            inicio = url.find('&')
            final = url.find('=')
            lista.append(url[inicio+1:final])
            url = url[final+1: len(url)]

            conta += 1

        return lista