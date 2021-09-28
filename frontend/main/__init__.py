import os
from flask import Flask
from dotenv import load_dotenv
from flask_wtf import CSRFProtect

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    csrf.init_app(app)
    from main.routes import inicio, main, iniciar_sesion, registrarse, ver_bolsones
    app.register_blueprint(routes.ver_bolsones.ver_bolsones)
    app.register_blueprint(routes.registrarse.registrarse)
    app.register_blueprint(routes.iniciar_sesion.iniciar_sesion)
    app.register_blueprint(routes.inicio.inicio)
    app.register_blueprint(routes.main.main)
    return app
