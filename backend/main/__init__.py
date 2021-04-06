import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resource as resources

api = Api()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    api.add_resource(resources.BolsonesResource, '/bolsones')
    api.add_resource(resources.BolsonResource, '/bolson/<id>')
    api.add_resource(resource.BolsonesPendientesResource, '/bolsonesprevios')
    api.add_resource(resource.BolsonPendienteResource, '/bolsonprevio/<id>')
    api.add_resource(resource.BolsonesPendientesResource, '/bolsonespendientes')
    api.add_resource(resource.BolsonPendienteResource, '/bolsonpendiente/<id>')
    api.add_resource(resource.BolsonesVentaResource, '/bolsonesventa')
    api.add_resource(resource.BolsonVentaResource, '/bolsonventa/<id>')
    api.add_resource(resource.ClientesResource, '/clientes')
    api.add_resource(resource.ClienteResource, '/cliente/<id>')
    api.add_resource(resource.ComprasResource, '/compras')
    api.add_resource(resource.CompraResource, '/compra/<id>')
    api.add_resource(resource.ProductosResource, '/productos')
    api.add_resource(resource.ProductoResource, '/producto/<id>')
    api.add_resource(resource.ProveedoresResource, '/proveedores')
    api.add_resource(resource.ProveedorResource, '/proveedor/<id>')
    api.init__app(app)
    return app
