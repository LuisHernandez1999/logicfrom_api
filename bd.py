import sqlite3

def criar_tabela_user():
   
    conexao = sqlite3.connect("usuarios.db")  
    cursor = conexao.cursor()
    
   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    
    conexao.commit() 
    conexao.close()  

if __name__ == "__main__":
    criar_tabela_user()
    print("Tabela 'users' criada com sucesso!")
