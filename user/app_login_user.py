from flask import Flask, request, jsonify
from user_functions import  validar_user
from models import User
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def api_login():
    try:
      
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')
        
      
        if not email or not senha:
            return jsonify({"message": "Email e senha são obrigatórios"}), 400
        
        
        if validar_user(email, senha):
           
            with sqlite3.connect("usuarios.db") as conexao:
                cursor = conexao.cursor()
                cursor.execute('''SELECT * FROM users WHERE email = ?''', (email,))
                user_data = cursor.fetchone()

            if user_data:
               
                user_obj = User(user_data[1], user_data[2], user_data[3], user_data[4])
                return jsonify({
                    "message": f"Login realizado com sucesso! Bem-vindo(a), {user_obj.nome}!",
                    "usuario": {
                        "nome": user_obj.nome,
                        "sobrenome": user_obj.sobrenome,
                        "email": user_obj.email
                    }
                }), 200
            else:
                return jsonify({"message": "Erro ao recuperar dados do usuário."}), 500
        else:
          
            return jsonify({"message": "Email ou senha incorretos."}), 401

    except Exception as e:
      
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
