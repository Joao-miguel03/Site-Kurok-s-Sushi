from flask import Blueprint, render_template, request, redirect, jsonify
import sqlite3 as sql 
from banco_dados.database import get_db

home_route = Blueprint('home', __name__)
logou = False

@home_route.route("/")
def home():
    return render_template("index.html")

# para logar
@home_route.route('/login', methods = ["GET", "POST"])
def logar():
    if request.method == "POST":

        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form

        percorrer_clientes = cursor.execute('select nome, email, senha from cliente')
        kuro_database.commit()
        percorrer_clientes = percorrer_clientes.fetchall()

        # consegui ajeitar a parte do login, por enquanto é só essa parte
        if percorrer_clientes != []:
            for i in percorrer_clientes:
                if i[0] == req['nome']:
                    if i[1] == req['email']:
                        if i[2] == req['senha']:
                            return redirect('/')
            return jsonify({'error': 'Não está cadastrado'})
        else:
            return redirect('/new')

    return render_template("login.html")
    
    #formulário para cadastrar um cliente
@home_route.route("/new/data", methods = ['POST'])
def inserir_client():
        kuro_database = sql.connect('banco_dados/kuro_database.db')
        kuro_database.row_factory = sql.Row
        cursor = kuro_database.cursor()

        req = request.json() # pega valores do formulario
        print(req)
        nome = req['nome']
        email = req['email']
        senha = req['senha']

        if not nome or not email or not senha:
            return jsonify({'error': 'Nome, Email e Senha são campos obrigatórios'})

        #fazer um id sempre diferente ds que eu tenho no banco de dados
        lista_id = cursor.execute('select id from cliente').fetchall()
        print(lista_id)

        if lista_id == []:
            id = 1
        else:
            for i in lista_id:
                print(i)
                id = len(lista_id) + 1
                if i == id:
                    id+=1

        cursor.execute(f'insert into cliente values ({id}, "{nome}", "{email}", "{senha}")')
        
        novo_cliente = cursor.execute(f'select * from cliente where id = {id}').fetchall()
        
        kuro_database.commit()
        
        return render_template('listar_cliente.html', clientes = novo_cliente)
        
@home_route.route('/new/data/form', methods = ['GET'])
def form_client():
    return render_template('form_client.html')

# listar os clientes
@home_route.route('/new/data')
def listar():
    kuro_database = get_db()
    cursor = kuro_database.cursor()

    dados = cursor.execute('select * from cliente').fetchall()
    if dados != []:
        return render_template('listar_cliente.html', clientes = dados)

@home_route.route('/new')
def crud():
    return render_template('crudCliente.html')

@home_route.route('/new/<int:dado_id>', methods = ['DELETE'])
def delete():
    return render_template('deletar_cliente.html')


@home_route.route('/config')
def configuracoes():
    return render_template('configuracao.html')