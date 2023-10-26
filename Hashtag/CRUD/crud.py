import mysql.connector


conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'usuario',
    password= 'senha',
    database= 'bdyoutube',
)

cursor = conexao.cursor()

#CRUD
comando = ''
cursor.execute(comando) 
conexao.commit() # edita o banco de dados
resultado = cursor.fetchall() # lê o banco de dados

cursor.close()
conexao.close()

# CREATE
nome_produto = "todynho"
valor = 3
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando) 
conexao.commit() # edita o banco de dados
resultado = cursor.fetchall() # lê o banco de dados

# READ
comando = f'SELECT * FROM bdyoutube.vendas'
cursor.execute(comando) 
resultado = cursor.fetchall() # lê o banco de dados
print(resultado)

#UPDATE
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando) 
conexao.commit() # edita o banco de dados

# DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando) 
conexao.commit() # edita o banco de dados
