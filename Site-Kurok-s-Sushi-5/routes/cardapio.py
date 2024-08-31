from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from banco_dados.database import get_db

cardapio_route = Blueprint('cardapio',__name__)

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