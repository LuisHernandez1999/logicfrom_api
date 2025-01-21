from flask import Flask, request, jsonify
from bd import criar_tabela_user
from funcao import criar_user, login
from classes import User
import sqlite3

app = Flask(__name__)

# Cria a tabela no banco de dados
criar_tabela_user()

@app.route('/criar_user', methods=['POST'])
def api_criar_user():
    print("Rota /criar_user chamada")
    try:
        # Recebe os dados no formato JSON
        data = request.get_json()
        print(f"Dados recebidos: {data}")
        
        # Coleta os dados enviados na requisição
        nome = data.get('nome')
        sobrenome = data.get('sobrenome')
        email = data.get('email')
        senha = data.get('senha')
        
        # Verifica se todos os campos foram fornecidos
        if not nome or not sobrenome or not email or not senha:
            return jsonify({"message": "Todos os campos são obrigatórios"}), 400
        
        print("Dados validados, tentando criar usuário...")
        # Chama a função criar_user para criar um novo usuário
        criar_user(nome, sobrenome, email, senha)
        
        # Recuperando o usuário do banco
        with sqlite3.connect("usuarios.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute('''SELECT * FROM users WHERE email = ?''', (email,))
            user_data = cursor.fetchone()

        if user_data:
            user_obj = User(user_data[1], user_data[2], user_data[3], user_data[4])
            return jsonify({
                "message": "Usuário criado com sucesso!",
                "usuario": {
                    "nome": user_obj.nome,
                    "sobrenome": user_obj.sobrenome,
                    "email": user_obj.email
                }
            }), 201
        else:
            return jsonify({"message": "Erro ao recuperar o usuário após criação."}), 500
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({"message": str(e)}), 500

@app.route('/login', methods=['POST'])
def api_login():
    try:
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')
        
        if not email or not senha:
            return jsonify({"message": "Email e senha são obrigatórios"}), 400
        
        resultado_login = login(email, senha)
        
        if resultado_login:
            user_obj = User(resultado_login['nome'], resultado_login['sobrenome'], resultado_login['email'], resultado_login['senha'])
            return jsonify({"message": f"Login realizado com sucesso! Bem-vindo(a), {user_obj.nome}!"}), 200
        else:
            return jsonify({"message": "Email ou senha incorretos."}), 401

    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
