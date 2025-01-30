import psycopg2

def validar_user(email, senha):
    try:
        # Estabelecendo a conexão com o banco PostgreSQL
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",  
            user="postgres",  
            password="luis27"  
        )
        
        cursor = conexao.cursor()

        # Executando a consulta SQL para verificar as credenciais do usuário
        cursor.execute('''SELECT * FROM users WHERE email = %s AND senha = %s''', (email, senha))
        
        user = cursor.fetchone()  # Obtém um único usuário correspondente

        # Verifica se o usuário foi encontrado
        if user:
            print(f"Usuário encontrado: {user[1]} {user[2]} (Email: {user[3]})")
            return True  # Retorna True se as credenciais forem válidas
        else:
            print("Usuário não encontrado ou credenciais incorretas.")
            return False  # Retorna False se o usuário não for encontrado ou as credenciais estiverem erradas
        
    except Exception as e:
        print(f"Erro ao validar o usuário: {str(e)}")
        return False  # Retorna False em caso de erro na consulta

    finally:
        # Fechando o cursor e a conexão com o banco
        if cursor:
            cursor.close() 
        if conexao:
            conexao.close() 
