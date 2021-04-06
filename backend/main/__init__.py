import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resource as resources

api = Api()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    api.add_resource(resources.bolsonesResource, '/bolsones')
    api.add_resource(resources.bolsonResource, '/bolson / <id>')
    api.add_resource(resource.bolsonespendientesResource, '/bolsonespendientes')
    api.add_resource(resource.bolsonpendienteResource, '/bolsonpendiente / <id>')
    api.add_resource(resource.bolsonesventaResource, '/bolsonesventa')
    api.add_resource(resource.bolsonventaResource, '/bolsonventa / <id>')
    api.add_resource(resource.clientesResource, '/clientes')
    api.add_resource(resource.clienteResource, '/cliente / <id>')
    api.add_resource(resource.comprasResource, '/compras')
    api.add_resource(resource.compraResource, '/compra / <id>')
    api.add_resource(resource.productosResource, '/productos')
    api.add_resource(resource.productoResource, '/producto / <id>')
    api.add_resource(resource.proveedoresResource, '/proveedores')
    api.add_resource(resource.proveedorResource, '/proveedor / <id>')
    api.init__app(app)
    return app
