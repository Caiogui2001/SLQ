import sqlite3

# Criar uma conexão com o banco de dados

conn = sqlite3.connect('mydatabase.db')

# Criar uma tabala

conn.execute('''CREATE TABLE stocks (date text , trans text , symbol text , qty real , price real)''')

# Salvar alterações 

conn.commit()

# Fechar a conexão com o banco de dados

conn.close()
