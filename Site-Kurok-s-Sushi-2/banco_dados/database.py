import sqlite3 as sql

# cria o banco de dados
kuro_database = sql.connect('banco_dados/kuro_database.db') 
# cria um objeto que vai gerenciar os comandos do meu banco de dados
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
    n_cartao integer not null, 
    senha_cartao integer not null, 
    cpf varchar(11) not null, 
    saldo float, 
    id_carteira integer primary key, 
    foreign key (id_carteira) references cliente(id)
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
print(lista_clientes)

kuro_database.commit()
kuro_database.close()