from flask import Flask, render_template, request

import sys
sys.path.append('f:\projetos\olistprojetos\marketplaces')

from backend.database import Database


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


database = Database('database.txt')

@app.route('/')
def index():
    name = 'Marketplaces'
    return render_template('index.html', name=name)


@app.route('/marketplaces')
def marketplaces():
    new_marketplace_name = request.args.get('new-marketplace')

    if new_marketplace_name != None:
        database.novo_marketplace(new_marketplace_name)

    marketplace = database.ler_marketplaces()

    name = 'Marketplaces List'

    return render_template('marketplaces.html', marketplace=marketplace, name=name)
    
@app.route('/categories')
def categories():
    name = 'Categories'

    categories_list = database.ler_categorias()


    return render_template('categories.html', list=categories_list, name=name)

@app.route('/subcategories')
def subcategories():

    name = "Subcategories"

    subcategories_list = database.ler_subcategorias()

    return render_template('subcategories.html', list=subcategories_list, name=name)


app.run(debug=True)
