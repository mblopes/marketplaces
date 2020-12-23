from flask import Flask, render_template

from category import Category
from subcategory import SubCategory
from marketplaces import Marketplaces

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


smartphones = SubCategory("Smartphones")
monitores = SubCategory("Monitores")

fogoes = SubCategory("Fogões")
geladeiras = SubCategory("Geladeiras")

eletronicos = Category("Eletrônicos", [smartphones, monitores])
cozinha = Category("Cozinha", [fogoes, geladeiras])

categories_list = [eletronicos, cozinha]

marketplaces_list = [Marketplaces("Americanas", categories_list)]

@app.route('/')
def index():
    name = 'Marketplaces'
    return render_template('index.html', name=name)

@app.route('/marketplaces')
def marketplaces():
    marketplace = marketplaces_list[0].name

    name = 'Marketplaces List'

    return render_template('marketplaces.html', marketplace=marketplace, name=name)
    
@app.route('/categories')
def categories():
    name = 'Categories'
    return render_template('categories.html', list=categories_list, name=name)

@app.route('/subcategories')
def subcategories():

    name = "Subcategories"

    return render_template('subcategories.html', eletronicos=eletronicos, cozinha=cozinha, smartphone=smartphones, monitores=monitores, fogoes=fogoes, geladeiras=geladeiras, name=name)


app.run(debug=True)
