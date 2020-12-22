from category import Category
from subcategory import SubCategory
from marketplaces import Marketplaces


eletronicos = Category("Eletrônicos", [SubCategory("Smartphones"), SubCategory("Monitores")])
cozinha = Category("Cozinha", [SubCategory("Fogões"), SubCategory("Geladeiras")])

categories_list = [eletronicos, cozinha]

marketplaces_list = [Marketplaces("Americanas", categories_list)]


def menu():
    options = ["Listar Marketplaces", "Listar Categorias", "Listar Subcategorias", "Sair"]

    for i, option in enumerate(options):
        print(f"{i+1} - {option}")
    
    option = int(input("Selecione uma opção: "))

    return option

def listar_marketplaces(marketplaces):
    for marketplace in marketplaces:
        print(marketplace.name)

def listar_categorias(marketplaces):
    for i, option in enumerate(marketplaces):
        print(f"{i} - {option.name}")
    
    option = int(input("Selecione uma opção: "))

    for category in marketplaces_list[option]:
        print(category.name)

def listar_sub_categorias(categories_list):
    for i, option in enumerate(categories_list):
        print(f"{i} - {option.name}")
    
    option = int(input("Selecione uma opção: "))

    for category in categories_list[option]:
        print(category.name)

while True:
    try:
        option = menu()

        if option == 1:
            listar_marketplaces(marketplaces_list)
        elif option == 2:
            listar_categorias(marketplaces_list)
        elif option == 3:
            listar_sub_categorias(categories_list)
        elif option == 4:
            exit(0)
        else:
            print("Opção indisponível. Tente novamente.")

    except ValueError:
        print("Opção indisponível. Tente novamente.")