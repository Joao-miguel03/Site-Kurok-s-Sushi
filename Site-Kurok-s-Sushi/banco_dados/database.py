import sqlite3

# cria o banco de dados
kuro_database = sqlite3.connect('Site-Kurok-s-Sushi/banco_dados/kuro_database.db') 

# cria um o bejeto que vai gerenciar os comandos do meu banco de dados
cursor = kuro_database.cursor() 

# .execute para executar um comando sql dentro do python
#cursor.execute(' CREATE TABLE clientes (id_cliente integer primary key, nome_cliente varchar(30) not null, email varchar(50) not null, senha varchar(10) not null)') 

#cursor.execute('insert into clientes values(1,"teste","teste.@teste.com","12345678");')
#cursor.execute('insert into clientes values(2,"miguel","miguel.@miguel.com","12345678");')


# teste se deu pra fazer assim então ta otimo acho q vou precisar de uma classe, falar com havana ou o próprio luciano
""""
id = 3
nome = 'nadla'
email = "nadla.com"
senha = "00800808"
cursor.execute(f'insert into clientes values({id},"{nome}","{email}","{senha}")')
"""

# .commit atualizar comandos no meu banco de dados
kuro_database.commit()

# mustrar no terminal minha tabela

# mais um teste tudo certo até aqui
"""id_cliente = cursor.execute('select id_cliente from clientes')
id_cliente = id_cliente.fetchall()
for i in range(len(id_cliente)):
    cliente = str(id_cliente[i])
    #id_cliente = int(id_cliente[2:len(id_cliente)-3])
    print(cliente[1:2])"""