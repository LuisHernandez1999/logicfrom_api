import sqlite3



def criar_user_na_tabela(nome, sobrenome, email, senha):
    """função para criar um usuário na tabela 'users'"""
    try:
        print("Criando um usuário na tabela de usuários...")
        conexao = sqlite3.connect("usuarios.db")  
        cursor = conexao.cursor()
        
        # inserção de um novo usuário na tabela 'users'
        cursor.execute('''
            INSERT INTO users (nome, sobrenome, email, senha) 
            VALUES (?, ?, ?, ?)
        ''', (nome, sobrenome, email, senha))
        
        conexao.commit()  # confirma a inserção
        print(f"Usuário {nome} {sobrenome} criado com sucesso!")
        
    except sqlite3.IntegrityError:
        print("Erro: O email já está registrado.")
    except Exception as e:
        print(f"Erro ao criar o usuário: {str(e)}")
    finally:
        conexao.close()  # fecha a conexão com o banco

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