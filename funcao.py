import sqlite3
from classes import User

def criar_user():
    nome = input('Entre seu nome: ')
    sobrenome = input('Entre seu sobrenome: ')
    email = input('Entre seu email: ')
    senha = input('Entre sua senha: ')
    
    confirmacao_senha = input('Confirme sua senha: ')
    while confirmacao_senha != senha:
        print("Senhas não são iguais. Por favor, tente novamente.")
        confirmacao_senha = input('Confirme sua senha: ')
    
    # conecta ao banco de dados
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    
    # inserir o usuário no banco de dados
    try:
        cursor.execute('''
            INSERT INTO users (nome, sobrenome, email, senha)
            VALUES (?, ?, ?, ?)
        ''', (nome, sobrenome, email, senha))
        conexao.commit()
        print(f"Usuário criado com sucesso!\nNome: {nome} {sobrenome}\nEmail: {email}")
    except sqlite3.IntegrityError:
        print(f"Erro: O email '{email}' já está em uso.")
    finally:
        conexao.close()

def login():
    email = input('Entre seu email: ')
    senha = input('Entre sua senha: ')
    
    
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    
   
    cursor.execute('''
        SELECT * FROM users WHERE email = ? AND senha = ?
    ''', (email, senha))
    user = cursor.fetchone()
    conexao.close()
    
    if user:
        print(f"Login realizado com sucesso! Bem-vindo(a), {User[1]}!")
    else:
        print("Email ou senha incorretos. Tente novamente.")


    

    
