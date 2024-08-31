from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from banco_dados.database import get_db

cliente_route = Blueprint('cliente',__name__)

# listar os clientes
@cliente_route.route('/')
def listar():
    kuro_database = get_db()
    cursor = kuro_database.cursor()

    dados = cursor.execute('select * from cliente').fetchall()
    if dados != []:
        return render_template('listar_cliente.html', clientes = dados)

    #formulário para cadastrar um cliente
@cliente_route.route("/form", methods = ['POST'])
def inserir_client():
        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form # pega valores do formulario
        nome = req['nome']
        email = req['email']
        senha = req['senha']

        if not nome or not email or not senha:
            return jsonify({'error': 'Nome, Email e Senha são campos obrigatórios'})

        #fazer um id sempre diferente do que eu tenho no banco de dados
        lista_id = cursor.execute('select id from cliente').fetchall()
        if lista_id == []:
            id = 1
        else:
            for i in lista_id:
                print(i)
                id = len(lista_id) + 1
                if int(str(i)[1]) == id:
                    id+=1

        cursor.execute(f'insert into cliente values ({id}, "{nome}", "{email}", "{senha}")')
        
        clientes = cursor.execute(f'select * from cliente').fetchall()
        kuro_database.commit()
        kuro_database.close
        return render_template('listar_cliente.html', clientes = clientes)
        
@cliente_route.route('/form', methods = ['GET'])
def form_client():
    return render_template('form_client.html')

#deletar
@cliente_route.route('/delete/<int:id>', methods = ['GET'])
def delete(id):
    kuro_database = get_db()
    cursor = kuro_database.cursor()

    cursor.execute(f'delete from cliente where id = {id}')
    kuro_database.commit()
    return redirect(url_for('cliente.listar'))

# editar usuario
@cliente_route.route('/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    if request.method == "POST":
        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form
        nome = req['nome']
        email = req['email']
        senha = req['senha']
        update =f"""
                    update cliente set
                        nome ="{nome}",
                        email = "{email}",
                        senha = "{senha}"
                    where id = {id}    
                """
        cursor.execute(update)
        kuro_database.commit()
        return redirect(url_for('cliente.listar'))
    kuro_database = get_db()
    cursor = kuro_database.cursor()
    cursor.execute(f'select * from cliente where id = {id}')
    data = cursor.fetchone()
    return render_template('edit_cliente.html', datas = data)
