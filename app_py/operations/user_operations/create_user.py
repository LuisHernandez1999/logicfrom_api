import psycopg2

def criar_user_na_tabela(nome, sobrenome, email, senha):
    """função para criar um usuário na tabela 'users'"""
    try:
        print("Criando um usuário na tabela de usuários...")
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",  # Nome do seu banco de dados
            user="postgres",  # Seu usuário do PostgreSQL
            password="luis27"  # Sua senha do PostgreSQL
        )
        cursor = conexao.cursor()
        
        # inserção de um novo usuário na tabela 'users'
        cursor.execute('''
            INSERT INTO users (nome, sobrenome, email, senha) 
            VALUES (%s, %s, %s, %s)
        ''', (nome, sobrenome, email, senha))
        
        conexao.commit()  # confirma a inserção
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