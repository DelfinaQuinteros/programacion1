from flask_restful import Resource
from flask import request

BOLSONESVENTA = {
    1: {'primer bolson venta': 'Bolson1'},
    2: {'segundo bolson venta': 'Bolson2'},
    3: {'tercer bolson venta': 'Bolson3'},
}


class Bolsonesventa(Resource):
    def get(self):
        return BOLSONESVENTA


class Bolsonventa(Resource):
    def get(self, id):
        if int(id) in BOLSONESVENTA:
            return BOLSONESVENTA[int(id)]
        return "", 404
