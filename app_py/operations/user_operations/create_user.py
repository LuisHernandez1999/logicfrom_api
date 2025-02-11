import psycopg2

def criar_user_na_tabela(nome, sobrenome, email, senha):
  
    try:
        print("Criando um usuário na tabela de usuários...")
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",  
            user="postgres",  
            password="luis27"  
        )
        cursor = conexao.cursor()
        
      
        cursor.execute('''
            INSERT INTO users (nome, sobrenome, email, senha) 
            VALUES (%s, %s, %s, %s)
        ''', (nome, sobrenome, email, senha))
        
        conexao.commit() 
        print(f"Usuário {nome} {sobrenome} criado com sucesso!")
        
    except psycopg2.IntegrityError:
        print("Erro: O email já está registrado.")
    except Exception as e:
        print(f"Erro ao criar o usuário: {str(e)}")
    finally:
        if cursor:
            cursor.close()  # fecha o cursor
        if conexao:
            conexao.close()  # fecha a conexão com o banco