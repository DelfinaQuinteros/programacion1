import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()


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
    return app
