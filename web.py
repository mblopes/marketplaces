from flask import Flask, render_template

from category import Category
from subcategory import SubCategory
from marketplaces import Marketplaces

app = Flask(__name__)

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
    return render_template('index.html')

@app.route('/marketplaces')
def marketplaces():

    return f'''
        <h1>Marketplaces</h1>
            <ul> 
                <li>{marketplaces_list[0].name}</li>
            </ul>

        <a href="/">Voltar<a>
    '''
    
@app.route('/categories')
def categories():
    return f'''
        <h1>Categorias</h1>
            <ul> 
                <li>{categories_list[0].name}</li>
                <li>{categories_list[1].name}</li>
            </ul>

        <a href="/">Voltar<a>
    '''

@app.route('/subcategories')
def subcategories():

    return f'''
        <h1>Categorias</h1>
            <ul> 
                <h2>{categories_list[0].name}</h2>
                    <li>{smartphones.name}</li>
                    <li>{monitores.name}</li>

                <h2>{categories_list[1].name}</h2>
                    <li>{fogoes.name}</li>
                    <li>{geladeiras.name}</li>
            </ul>

        <a href="/">Voltar<a>
    '''


app.run(debug=True)
