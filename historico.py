import json

class Historico:

    def __init__(self, caminho):
        self.arquivo = open(caminho, 'r')
        self.marketplaces = self.arquivo.readlines()

        self.marketplaces_list = []

        for self.marketplace in self.marketplaces:
            self.dados = json.loads(self.marketplace)
            self.marketplaces_list.append(self.dados)

        self.arquivo.close()
    
    def ler_marketplaces(self):
        self.marketplaces_nomes = []
        for self.marketplace in self.marketplaces_list:
            self.marketplaces_nomes.append(self.marketplace["nome"])
    
        return self.marketplaces_nomes
    
    def ler_categorias(self):
        self.lista_categorias = []

        for self.marketplace in self.marketplaces_list:
            for self.categoria in self.marketplace["categorias"]:
                self.lista_categorias.append(self.categoria)
        
        return self.lista_categorias
    
    def ler_subcategorias(self):
        self.lista_subcategorias = []

        for self.marketplace in self.marketplaces_list:
            for self.subcategoria in self.marketplace["subcategorias"]:
                self.lista_subcategorias.append(self.subcategoria)
        
        return self.lista_subcategorias

