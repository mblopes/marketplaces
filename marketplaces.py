class Marketplaces:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

magazine = Marketplaces("Magazine")

print(magazine.nome)

magazine.nome("Americanas")
print(magazine.nome)