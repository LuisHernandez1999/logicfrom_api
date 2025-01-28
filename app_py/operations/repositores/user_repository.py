# repositories/user_repository.py
import sqlite3
from datetime import datetime

# Função para validar o login de um usuário
def validar_user(email, senha):
    with sqlite3.connect("usuarios.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM users WHERE email = ? AND senha = ?''', (email, senha))
        user_data = cursor.fetchone()
        return user_data is not None

# Função para obter os dados do usuário pelo email
def get_user_data(email):
    with sqlite3.connect("usuarios.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM users WHERE email = ?''', (email,))
        user_data = cursor.fetchone()
        
        if user_data:
            return {
                "id": user_data[0],
                "nome": user_data[1],
                "sobrenome": user_data[2],
                "email": user_data[3]
            }
        else:
            return None  # Retorna None se não encontrar o usuário

# Função para inserir um usuário no banco de dados
def insert_user_into_db(nome, sobrenome, email, senha):
    with sqlite3.connect("usuarios.db") as conexao:
        cursor = conexao.cursor()

        # Insere os dados do usuário na tabela 'users'
        cursor.execute('''
            INSERT INTO users (nome, sobrenome, email, senha)
            VALUES (?, ?, ?, ?)
        ''', (nome, sobrenome, email, senha))

        conexao.commit()
