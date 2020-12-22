from category import Category
from subcategory import SubCategory
from marketplaces import Marketplaces


eletronicos = Category("Eletrônicos", [SubCategory("Smartphones"), SubCategory("Monitores")])
cozinha = Category("Cozinha", [SubCategory("Fogões"), SubCategory("Geladeiras")])

marketplaces = [Marketplaces("Americanas", [eletronicos, cozinha])]

for marketplace in marketplaces:
    print(f"Marketplace: {marketplace.name}")
    print("Categorias:")
    for category in marketplace:
        print("---------------------------")
        print(f"{category.name}\n")
        print("Subcategorias:")
        for sub_category in category:
            print(sub_category.name)