import os
from flask import Flask
from dotenv import load_dotenv
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_required

csrf = CSRFProtect()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['API_URL'] = os.getenv('API_URL')
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    csrf.init_app(app)
    login_manager.init_app(app)
    from main.routes import inicio, main, cliente
    app.register_blueprint(routes.cliente.cliente)
    app.register_blueprint(routes.inicio.inicio)
    app.register_blueprint(routes.main.main)
    return app
