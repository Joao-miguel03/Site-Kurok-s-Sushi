import sqlite3

# cria o banco de dados
kuro_database = sqlite3.connect('banco_dados/kuro_database.db') 

# cria um o bejeto que vai gerenciar os comandos do meu banco de dados
cursor = kuro_database.cursor() 

#cursor.execute('create table cliente(id integer, nome varchar(40), email varchar(40) not null, senha varchar(8) not null, primary key(id, nome))')
#cursor.execute('create table carteira(n_cartao integer not null, senha_cartao integer not null, cpf varchar(11) not null, saldo float, nome varchar (40), id_carteira integer primary key, foreign key (id_carteira, nome) references cliente(id, nome))')
#cursor.execute('create table cardapio(id_comida integer primary key, comida varchar(30) not null, preco float, estrelas integer, comentario varchar(40))') 

kuro_database.commit()