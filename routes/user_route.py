from flask import Flask, render_template, redirect, url_for, request, session, Blueprint
from models import Book
from serverDatabase import getInfoItems, getLocais, getIdItems, getIdLocais, registerItem_locais

user_bp = Blueprint('user', __name__ , template_folder='templates')

@user_bp.route('/')
def home():
    lista_locais = getLocais()
    name = session.get('user')

    return render_template('home.html', name= name, lista_locais = lista_locais)

@user_bp.route('/cad', methods=["POST","GET"])
def cadastrarItems():
    locais = getIdLocais()
    items = getIdItems()
    dados = getLocais()
    return render_template('registerItem.html', locais = locais, items = items, dados = dados)

@user_bp.route('/add_item_local', methods=['GET', 'POST'])
def addItemLocal():
    local = request.form.get('local_id')
    item = request.form.get('item_id')
    qnt = request.form.get('quantidade')

    requestDb = registerItem_locais(local, item, qnt)
    return redirect('/', vf = requestDb)


@user_bp.before_request
def check_validation():
    if 'token' not in session:
        return redirect('/auth')
    
