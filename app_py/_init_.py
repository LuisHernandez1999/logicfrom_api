from flask import Flask
from app_py.routes.user_routes import user_routes

app = Flask(__name__)

# Registra as rotas no aplicativo
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=True)
    