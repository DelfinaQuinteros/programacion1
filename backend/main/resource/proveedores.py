from flask_restful import Resource
from flask import request

PROFESSORS = {
    1: {'firstname': 'aa', 'lastname': 'bb'},
    2: {'firstname': 'cc', 'lastname': 'dd'},
}


class Proveedores(Resource):
    def get(self):
        return ''

    def post(self):
        return ''


class Proveedor(Resource):
    def get(self):
        return ""

    def delete(self):
        return ''

    def put(self):
        return ''
