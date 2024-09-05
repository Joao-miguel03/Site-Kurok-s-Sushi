from flask import Blueprint, render_template, request, redirect, jsonify, url_for, flash
from banco_dados.database import get_db

cardapio_route = Blueprint('cardapio',__name__)


@cardapio_route.route('/<int:id_pessoa>')
def cardapio(id_pessoa):
    kuro_database = get_db()
    cursor = kuro_database.cursor()
    
    cardapio = cursor.execute('select * from cardapio').fetchall()

    return render_template('cardapio.html', cardapio = cardapio, id_pessoa = id_pessoa)

@cardapio_route.route('/<int:id_pessoa>/<int:id_item>', methods = ['GET'])
def item_cardapio(id_pessoa,id_item):
    kuro_database = get_db()
    cursor = kuro_database.cursor()
    cursor.execute(f'select * from cardapio where id_comida = {id_item}')
    data = cursor.fetchone()

    return render_template('item_cardapio.html', item = data, id_pessoa = id_pessoa)

@cardapio_route.route('<int:id_pessoa>/<int:id_item>/comprar', methods = ["GET","POST"])
def comprar(id_pessoa,id_item):
    if request.method == "POST":
        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form
        qtd = float(req['qtd'])
        preco = cursor.execute(f'select preco from cardapio where id_comida = {id_item}').fetchone()[0]
        preco = qtd * preco
        saldo = cursor.execute(f'select * from carteira').fetchall()
        print(preco)
    
        for i in saldo:
            if i[0] == id_pessoa:
                print(id_pessoa)
                saldo = i[4]
        
        print(saldo)
        saldo = saldo - preco
        if saldo >= 0:
            cursor.execute(f'update carteira set saldo = {saldo} where id_carteira = {id_pessoa}')
            comprado = True
        elif saldo < 0 :
            comprado = False
        kuro_database.commit()

        # if comprado == True:
        #     flash("Compra efetuada com sucesso")
        # elif comprado == False:
        #     flash("Saldo insuficiente")

        return redirect(url_for('home.menu', id = id_pessoa))
    return render_template('compra.html', id_pessoa = id_pessoa, id_item = id_item)


@cardapio_route.route('/data')
def listar():
    kuro_database = get_db()
    cursor = kuro_database.cursor()
    cardapio = cursor.execute('select * from cardapio').fetchall()

    return render_template('listar_cardapio.html', cardapio = cardapio)


@cardapio_route.route('/data/form', methods = ['POST','GET']) 
def form_cardapio():
    if request.method == "POST":
        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form

        nome = req['nome']
        preco = req['preco']
        estrelas = req['estrelas']
        descricao = req['descricao']

        lista_id = cursor.execute('select id_comida from cardapio').fetchall()
        if lista_id == []:
            id = 1
        else:
            for i in lista_id:
                print(i)
                id = len(lista_id) + 1
                if int(str(i)[1]) == id:
                    id+=1

        cursor.execute(f'insert into cardapio values ({id},"{nome}",{preco},{estrelas},"{descricao}")')

        cardapio = cursor.execute(f'select * from cardapio').fetchall()
        kuro_database.commit()

        return redirect(url_for('cardapio.listar'))
    return render_template('form_cardapio.html')

#deletar
@cardapio_route.route('/data/delete/<int:id>', methods = ['GET'])
def delete(id):
    kuro_database = get_db()
    cursor = kuro_database.cursor()

    cursor.execute(f'delete from cardapio where id_comida = {id}')
    kuro_database.commit()
    return redirect(url_for('cardapio.listar'))

# editar usuario
@cardapio_route.route('/data/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    if request.method == "POST":
        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form
        nome = req['nome']
        preco = req['preco']
        estrelas = req['estrelas']
        descricao = req['descricao']
        update =f"""
                    update cardapio set
                        comida ="{nome}",
                        preco = "{preco}",
                        estrelas = "{estrelas}",
                        comentario = "{descricao}"
                    where id_comida = {id}    
                """
        cursor.execute(update)
        kuro_database.commit()

        return redirect(url_for('cardapio.listar'))
    kuro_database = get_db()
    cursor = kuro_database.cursor()
    cursor.execute(f'select * from cardapio where id_comida = {id}')
    data = cursor.fetchone()

    return render_template('edit_cardapio.html', datas = data)