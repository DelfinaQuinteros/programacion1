import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail


from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
jwt = JWTManager()
mailsender = Mail()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    if not os.path.exists(os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME')
    db.init_app(app)
    import main.resources as resources
    api.add_resource(resources.BolsonesResource, '/bolsones')
    api.add_resource(resources.BolsonResource, '/bolson/<id>')
    api.add_resource(resources.BolsonesVentaResource, '/bolsonesventa')
    api.add_resource(resources.BolsonVentaResource, '/bolsonventa/<id>')
    api.add_resource(resources.BolsonesPendientesResource, '/bolsonespendientes')
    api.add_resource(resources.BolsonPendienteResource, '/bolsonpendiente/<id>')
    api.add_resource(resources.BolsonesPreviosResource, '/bolsonesprevios')
    api.add_resource(resources.BolsonPrevioResource, '/bolsonprevio/<id>')
    api.add_resource(resources.ProductosResource, '/productos')
    api.add_resource(resources.ProductoResource, '/producto/<id>')
    api.add_resource(resources.ComprasResource, '/compras')
    api.add_resource(resources.CompraResource, '/compra/<id>')
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    api.add_resource(resources.ProveedoresResource, '/proveedores')
    api.add_resource(resources.ProveedorResource, '/proveedor/<id>')
    api.add_resource(resources.ProductosBolsonesResource, '/productos-bolsones')
    api.add_resource(resources.ProductoBolsonResource, '/producto-bolson/<id>')
    api.init_app(app)

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    from main.auth import Routes
    app.register_blueprint(auth.Routes.auth)

    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')
    mailsender.init_app(app)

    return app
