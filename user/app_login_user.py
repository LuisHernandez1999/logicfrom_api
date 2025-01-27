from flask import Flask, request, jsonify
from user_functions import validar_user
from models import User
import sqlite3
from datetime import datetime,timedelta
import jwt

app = Flask(__name__)

SECRET_WORD_FOR_LOGIN = ""
@app.route('/login', methods=['POST'])
def api_login():
    try:
        # recebe os dados no formato JSON
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')
        
        # verifica se ambos os campos foram preenchidos
        if not email or not senha:
            return jsonify({"message": "Email e senha são obrigatórios"}), 400
        
        # valida o usuário
        if validar_user(email, senha):
            # conecta ao banco e recupera os dados do usuário
            with sqlite3.connect("usuarios.db") as conexao:
                cursor = conexao.cursor()
                cursor.execute('''SELECT * FROM users WHERE email = ?''', (email,))
                user_data = cursor.fetchone()

            if user_data:
                # cria o objeto do usuário
                user_obj = User(user_data[1], user_data[2], user_data[3], user_data[4])
                
                # registra a data e hora do login
                data_hora_do_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{user_obj.nome} fez login em {data_hora_do_login}")
                
                # define o status do usuário
                status = "online e logado"
                print(f"{user_obj.nome} está {status}")
                
                token_payload = {
                    "nome": user_obj.nome,
                    "email": user_obj.email,
                    "exp": datetime.utcnow() + timedelta(hours=1)  # expiração do token 1hora nessa porra 
                }
                token = jwt.encode(token_payload, SECRET_WORD_FOR_LOGIN, algorithm="HS256")

                # retorna a resposta
                return jsonify({
                    "message": f"Login realizado com sucesso! Bem-vindo(a), {user_obj.nome}!",
                    "usuario": {
                        "nome": user_obj.nome,
                        "sobrenome": user_obj.sobrenome,
                        "email": user_obj.email,
                        "status": status,
                        "hora_do_login": data_hora_do_login
                    },
                    "token": token
                }), 200
            else:
                return jsonify({"message": "Erro ao recuperar dados do usuário."}), 500
        else:
            # login inválido
            return jsonify({"message": "Email ou senha incorretos."}), 401

    except Exception as e:
      
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
