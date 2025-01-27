from flask import Flask, request, jsonify
from models import User
import sqlite3
from user_functions import  criar_user_na_tabela
from bd import criar_tabela_user

app = Flask(__name__)


criar_tabela_user()

@app.route('/criar_user', methods=['POST'])
def api_criar_user():
    print("Rota /criar_user chamada")
    try:
        # recebe os dados no formato JSON
        data = request.get_json()
        print(f"Dados recebidos: {data}")
        
        
        nome = data.get('nome')
        sobrenome = data.get('sobrenome')
        email = data.get('email')
        senha = data.get('senha')
        
       
        if not nome or not sobrenome or not email or not senha:
            return jsonify({"message": "Todos os campos são obrigatórios"}), 400
        
        print("Dados validados, tentando criar usuário...")
        
        # chama a função para criar o usuário no banco de dados
        criar_user_na_tabela(nome, sobrenome, email, senha)
        
       
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
            return jsonify({"message": "Erro na criação de usuário."}), 500
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
