import sqlite3 as sql

# Função para conectar ao banco de dados
def get_db():
    kuro_database = sql.connect('banco_dados/kuro_database.db')
    return kuro_database

kuro_database = get_db()
cursor = kuro_database.cursor()

table_cliente = """
create table cliente(
    id integer, 
    nome varchar(40),
    email varchar(40) not null ,
    senha varchar(8) not null,
    primary key(id) )
"""
table_carteira = """
create table carteira(

    id_carteira integer primary key,

    n_cartao integer not null, 
    senha_cartao integer not null, 
    cpf varchar(11) not null, 
    saldo float, 

    foreign key (id_carteira) references cliente(id)
    ON UPDATE SET NULL
    ON DELETE SET NULL
)
"""
table_cardapio =""" 
create table cardapio(
    id_comida integer primary key, 
    comida varchar(30) not null, 
    preco float, 
    estrelas integer, 
    comentario varchar(40)
)
"""
table_vendas = """


"""


'''
cursor.execute('drop table if exists cliente')
cursor.execute('drop table if exists carteira')
cursor.execute('drop table if exists cardapio')
'''

'''
cursor.execute(table_cardapio)
cursor.execute(table_carteira)
cursor.execute(table_cliente)
'''

# cursor.execute('insert into cliente values(1,"teste", "email@gg", "1234")')

lista_clientes = cursor.execute('select * from cliente').fetchall()
kuro_database.commit()
print(lista_clientes)

kuro_database.close()