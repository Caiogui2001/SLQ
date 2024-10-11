import sqlite3

# Criar uma conexão com o banco de dados 

conn = sqlite3.connect('mydatabase.db')

# Atualizar dados na tabela
valor_usuario = float(input('Informe o valor :'))
conn.execute(f'UPDATE stocks SET price = {valor_usuario} WHERE symbol = "RHAT"')

# Salvar as alterações 

conn.commit()

# Fechar conexão com o banco de dados

conn.close()