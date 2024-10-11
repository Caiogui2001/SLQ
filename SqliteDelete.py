import sqlite3

# Criar uma conexão com o banco de dados

conn = sqlite3.connect('mydatabase.db')

# Deletar dados da tabela

conn.execute('DELETE from stocks WHERE symbol = "IBM"')

# Salvar as alterações

conn.commit()

# Fechar a conexão com o banco de dados

conn.close()