import psycopg2


DB_HOST = "localhost" 
DB_NAME = "moneycontroltwo"  
DB_USER = "postgres"  
DB_PASSWORD = "luis27" 


def criar_banco():
    conexao = None  
    cursor = None  
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database="postgres",  
            client_encoding='UTF8'  
        )
        conexao.autocommit = True  
        cursor = conexao.cursor()


       
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
        existe = cursor.fetchone()

        if not existe:
            cursor.execute(f"CREATE DATABASE {DB_NAME} ENCODING 'UTF8';") 
            print(f"Banco '{DB_NAME}' criado com sucesso!")
        else:
            print(f"Banco '{DB_NAME}' já existe.")

    except Exception as e:
        print(f"Erro ao criar banco: {e}")

    finally:
        if cursor:  
            cursor.close()
        if conexao:  
            conexao.close()
        print("Conexão encerrada.")


def criar_tabela_user():
    print("Criando a tabela de usuários...")

    conexao = None  
    cursor = None  
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            client_encoding='UTF8' 
        )
        cursor = conexao.cursor()

    
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                sobrenome VARCHAR(100) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')

        conexao.commit()
        print("Tabela 'users' criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

    finally:
        if cursor:  
            cursor.close()
        if conexao: 
            conexao.close()
        print("Conexão encerrada.")


def criar_tabela_gastos():
    print("Criando a tabela de gastos...")

    conexao = None
    cursor = None
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            client_encoding='UTF8'
        )
        cursor = conexao.cursor()

       
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gastos (
                id SERIAL PRIMARY KEY,
                id_user INTEGER REFERENCES users(id) ON DELETE CASCADE,
                nome VARCHAR(255) NOT NULL,
                data DATE DEFAULT CURRENT_DATE,
                valor DECIMAL(10,2) NOT NULL,
                categoria VARCHAR(50) CHECK (categoria IN (
                    'contas', 'lazer', 'estudos', 'streaming', 
                    'delivery', 'supermercado', 'shopping'
                )) NOT NULL
            )
        ''')

        conexao.commit()
        print("Tabela 'gastos' criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        print("Conexão encerrada.")


def criar_tabela_ganhos():
    print("Criando a tabela de ganhos...")

    conexao = None
    cursor = None
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            client_encoding='UTF8'
        )
        cursor = conexao.cursor()

     
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS ganhos (
                id SERIAL PRIMARY KEY,
                id_user INTEGER REFERENCES users(id) ON DELETE CASCADE,
                nome VARCHAR(255) NOT NULL,
                data DATE DEFAULT CURRENT_DATE,
                valor DECIMAL(10,2) NOT NULL,
                categoria VARCHAR(50) CHECK (categoria IN (
                    'salário', 'renda extra', 'freelance'
                )) NOT NULL
            )
        ''')

        conexao.commit()
        print("Tabela 'ganhos' criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        print("Conexão encerrada.")


if __name__ == "__main__":
    criar_banco()  
    criar_tabela_user() 
    criar_tabela_gastos()
    criar_tabela_ganhos()
