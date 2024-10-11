import sqlite3

# Criar uma conexão com o banco de dados

conn = sqlite3.connect('mydatabase.db')

# Selecionar todos os dados da tabela

cursor = conn.execute('SELECT price from stocks')

# Iterar sobre o dados e exibi-los

for row in cursor:
    print(row)
    
# Fechar a conexão com o banco de dados

conn.close()