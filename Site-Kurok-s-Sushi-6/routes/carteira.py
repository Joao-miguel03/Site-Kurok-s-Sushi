from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from banco_dados.database import get_db

carteira_route = Blueprint('carteira',__name__)

# listar os clientes
@carteira_route.route('/')
def listar():
    kuro_database = get_db()
    cursor = kuro_database.cursor()
    carteiras = cursor.execute('select * from carteira').fetchall()

    return render_template('listar_carteira.html', carteiras = carteiras)


# deletar carteira
@carteira_route.route('/delete/<int:id>', methods = ['GET'])
def delete(id):
    kuro_database = get_db()
    cursor = kuro_database.cursor()

    cursor.execute(f'delete from carteira where id_carteira = {id}')
    kuro_database.commit()
    return redirect(url_for('carteira.listar'))

# editar carteira
@carteira_route.route('/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    if request.method == "POST":
        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form
        n_cartao = req['n_cartao']
        senha_cartao = req['senha_cartao']
        cpf = req['cpf']
        saldo = req['saldo']
        update =f"""
                    update carteira set
                        n_cartao ="{n_cartao}",
                        senha_cartao = "{senha_cartao}",
                        cpf = "{cpf}",
                        saldo = {saldo}
                    where id_carteira = {id}    
                """
        cursor.execute(update)
        kuro_database.commit()
        return redirect(url_for('carteira.listar'))
    
    kuro_database = get_db()
    cursor = kuro_database.cursor()

    cursor.execute(f'select * from carteira where id_carteira = {id}')

    data = cursor.fetchone()
    return render_template('edit_carteira.html', datas = data)
