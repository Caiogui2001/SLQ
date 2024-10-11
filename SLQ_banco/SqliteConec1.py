import sqlite3

# Criar uma conexão com o banco de dados

conn = sqlite3.connect('Automoveis.db')

# Criar uma tabala

conn.execute('''CREATE TABLE stocks (Modelo text , cor text , ano int)''')

# Salvar alterações 

conn.commit()

# Fechar a conexão com o banco de dados

conn.close()