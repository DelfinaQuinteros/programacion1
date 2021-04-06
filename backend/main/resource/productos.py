from flask_restful import Resource
from flask import request

PRODUCTOS = {
    1: {'primer producto': '1er producto'},
    2: {'segundo producto': '2do producto'}
}


class Productos(Resource):
    def get(self):
        return PRODUCTOS


class Producto(Resource):
    def get(self, id):
        if int(id) in PRODUCTOS:
            return PRODUCTOS[int(id)]
        return "", 404
