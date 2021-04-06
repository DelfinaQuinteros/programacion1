from flask_restful import Resource
from flask import request

BOLSONESPREVIOS = {
    1: {'primer bolson previo': 'Bolson1'},
    2: {'segundo bolson previo': 'Bolson2'},
    3: {'tercer bolson previo': 'Bolson3'},
}


class Bolsonesprevios(Resource):
    def get(self):
        return BOLSONESPREVIOS


class Bolsonprevio(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return "", 404
