import json
from date import retorna_data

class Database:

    def __init__(self, caminho):
        self.caminho = caminho
    
    def consultar_dados(self):
        self.arquivo = open(self.caminho, 'r')
        self.marketplaces = self.arquivo.readlines()

        self.marketplaces_list = []

        for self.marketplace in self.marketplaces:
            self.dados = json.loads(self.marketplace)
            self.marketplaces_list.append(self.dados)

        self.arquivo.close()

        return self.marketplaces_list
    
    def ler_marketplaces(self) -> list:
        self.marketplaces_list = self.consultar_dados()

        self.marketplaces_nomes = []
        for self.marketplace in self.marketplaces_list:
            self.marketplaces_nomes.append(self.marketplace["nome"])
        
        self.log = open("log.txt", "a")
        self.log.write(f'{retorna_data()} - Marketplaces listados\n')
        self.log.close()
    
        return self.marketplaces_nomes
    
    def ler_categorias(self) -> list:
        self.marketplaces_list = self.consultar_dados()

        self.lista_categorias = []

        for self.marketplace in self.marketplaces_list:
            for self.categoria in self.marketplace["categorias"]:
                self.lista_categorias.append(self.categoria)
        
        self.log = open("log.txt", "a")
        self.log.write(f'{retorna_data()} - Categorias listadas\n')
        self.log.close()
        
        return self.lista_categorias
    
    def ler_subcategorias(self) -> list:
        self.marketplaces_list = self.consultar_dados()

        self.lista_subcategorias = []

        for self.marketplace in self.marketplaces_list:
            for self.subcategoria in self.marketplace["subcategorias"]:
                self.lista_subcategorias.append(self.subcategoria)
        
        self.log = open("log.txt", "a")
        self.log.write(f'{retorna_data()} - Subcategorias listadas\n')
        self.log.close()
        
        return self.lista_subcategorias
    
    def novo_marketplace(self, nome):
        self.arquivo = open(self.caminho, 'a')

        self.nome = f'"nome":"{nome}",'
        self.categorias = f'"categorias": ["Eletronico","Cozinha"],'
        self.subcategorias = f'"subcategorias": ["Smartphone", "Videogames", "Talheres", "Pratos"]'
        
        self.arquivo.write('{' + self.nome + self.categorias + self.subcategorias + '}\n')

        self.arquivo.close()
