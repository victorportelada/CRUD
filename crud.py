import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='*******',
        database='bdcrud'
    )

def create(nome_produto, valor):
    conexao = connect_to_db()
    cursor = conexao.cursor()
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
    cursor.execute(comando, (nome_produto, valor))
    conexao.commit()
    cursor.close()
    conexao.close()

def read():
    conexao = connect_to_db()
    cursor = conexao.cursor()
    comando = 'SELECT * FROM vendas;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def update(nome_produto, valor):
    conexao = connect_to_db()
    cursor = conexao.cursor()
    comando = f'UPDATE vendas SET valor = %s WHERE nome_produto = %s'
    cursor.execute(comando, (valor, nome_produto))
    conexao.commit()
    cursor.close()
    conexao.close()

def delete(nome_produto):
    conexao = connect_to_db()
    cursor = conexao.cursor()
    comando = f'DELETE FROM vendas WHERE nome_produto = %s'
    cursor.execute(comando, (nome_produto,))
    conexao.commit()
    cursor.close()
    conexao.close()

# Testando as funções

create('chocolate', 15)
print(read())
update('chocolate', 20)
print(read())
delete('chocolate')
print(read())
