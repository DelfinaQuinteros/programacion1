from flask_restful import Resource
from flask import request

BOLSONESPENDIENTES = {
    1: {'primer bolson pendiente': 'Bolson1'},
    2: {'segundo bolson pendiente': 'Bolson2'},
    3: {'tercer bolson pendiente': 'Bolson3'},
}


class BolsonesPendientes(Resource):
    def get(self):
        return BOLSONESPENDIENTES

    def post(self):
        bolsonpendiente = request.get_json()
        id = int(max(BOLSONESPENDIENTES.keys())) + 1
        BOLSONESPENDIENTES[id] = bolsonpendiente
        return BOLSONESPENDIENTES[int(id)], 201


class BolsonPendiente(Resource):
    def get(self, id):
        if int(id) in BOLSONESPENDIENTES:
            return BOLSONESPENDIENTES[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in BOLSONESPENDIENTES:
            del BOLSONESPENDIENTES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in BOLSONESPENDIENTES:
            bolsonprevio = BOLSONESPENDIENTES[int(id)]
            date = request.get_json()
            bolsonprevio.update(date)
            return bolsonprevio, 201
        return '', 404
