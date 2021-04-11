from flask_restful import Resource
from flask import request

PRODUCTOS = {
    1: {'primer producto': '1er producto'},
    2: {'segundo producto': '2do producto'}
}


class Productos(Resource):
    def get(self):
        return PRODUCTOS

    def post(self):
        producto = request.get_json()
        id = int(max(PRODUCTOS.keys())) + 1
        PRODUCTOS[int(id)] = producto
        return PRODUCTOS[int(id)], 201


class Producto(Resource):
    def get(self, id):
        if int(id) in PRODUCTOS:
            return PRODUCTOS[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in PRODUCTOS:
            del PRODUCTOS[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in PRODUCTOS:
            producto = PRODUCTOS[int(id)]
            date = request.get_json()
            producto.update(date)
            return producto, 201
        return '', 404
