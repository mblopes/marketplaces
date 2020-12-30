from database import Database

database = Database('database.txt')

def menu():
    options = ["Listar Marketplaces", "Listar Categorias", "Listar Subcategorias", "Sair"]

    for i, option in enumerate(options):
        print(f"{i+1} - {option}")
    
    option = int(input("Selecione uma opção: "))

    return option

def listar_marketplaces(marketplaces):
    for marketplace_name in marketplaces:
        print(marketplace_name)

def listar_categorias(categories_list):
    for category in categories_list:
        print(category)

def listar_sub_categorias(subcategories_list):
    for subcategory in subcategories_list:
        print(subcategory)

while True:
    try:
        option = menu()

        if option == 1:
            listar_marketplaces(database.ler_marketplaces())
        elif option == 2:
            listar_categorias(database.ler_categorias())
        elif option == 3:
            listar_sub_categorias(database.ler_subcategorias())
        elif option == 4:
            exit(0)
        else:
            print("Opção indisponível. Tente novamente.")

    except ValueError:
        print("Opção indisponível. Tente novamente.")