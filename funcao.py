#funcaos que irá ultilizar o classe
import sqlite3
from classes import User

def criar_user(nome, sobrenome, email, senha):
    print(f"Criando usuário {nome} {sobrenome}")
    novo_usuario = User(nome, sobrenome, email, senha)
    
    with sqlite3.connect("usuarios.db") as conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (nome, sobrenome, email, senha)
                VALUES (?, ?, ?, ?)
            ''', (novo_usuario.nome, novo_usuario.sobrenome, novo_usuario.email, novo_usuario.senha))
            conexao.commit()
            print(f"Usuário {nome} {sobrenome} criado no banco de dados.")
        except sqlite3.IntegrityError:
            raise Exception(f"O email '{novo_usuario.email}' já está em uso.")

def login(email, senha):
    with sqlite3.connect("usuarios.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE email = ? AND senha = ?
        ''', (email, senha))
        user_data = cursor.fetchone()

    if user_data:
        return {"nome": user_data[1], "sobrenome": user_data[2], "email": user_data[3]}
    else:
        return None
