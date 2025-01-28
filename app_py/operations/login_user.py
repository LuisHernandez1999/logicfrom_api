import sqlite3
def validar_user(email, senha):
    """função para validar um usuário pelo email e senha"""
    try:
        conexao = sqlite3.connect("usuarios.db")
        cursor = conexao.cursor()

        
        cursor.execute('''
            SELECT * FROM users WHERE email = ? AND senha = ?
        ''', (email, senha))
        
        user = cursor.fetchone() 

        if user:
            print(f"Usuário encontrado: {user[1]} {user[2]} (Email: {user[3]})")
            return True  #
          
        else:
            print("Usuário não encontrado ou credenciais incorretas.")
            return False  
        
    except Exception as e:
        print(f"Erro ao validar o usuário: {str(e)}")
        return False
    finally:
        conexao.close()  # Fecha a conexão com o banco