import sqlite3

# Criar uma conexão com o banco de dados

conn = sqlite3.connect('Automoveis.db')

def menu():
    while True:
        print("\nMenu:")
        print('1 - Inserir')
        print('2 - Deletar ')
        print('3 - Ler')
        print('0 - Sair')

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            modelo = input('Informe o modelo: ')
            cor = input('Informe a cor: ')
            ano = int(input('Informe o ano: '))
            conn.execute('INSERT INTO stocks (modelo, cor, ano) VALUES (?, ?, ?)', (modelo, cor, ano))
            conn.commit()
            print("Automóvel inserido com sucesso!")
        
        elif opcao == '2':
            
            deletar = input('Qual você deseja deletar (MODELO, COR , ANO):').strip().lower()
            if deletar not in ['modelo' , 'cor' , 'ano']:
                print("Opção inválida! Tente novamente.")
                continue
            valor = input(f'Qual {deletar} deseja deletar? ')
            conn.execute(f'DELETE FROM stocks WHERE {deletar} = ?', (valor,))
            print('Deletado com sucesso')
            conn.commit()
            
        
        elif opcao == '3':
            conn.execute('SELECT * FROM stocks')
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
            

menu()    
# Salvar as alterações

conn.commit()

# Fechar a conexão com o banco de dados

conn.close()