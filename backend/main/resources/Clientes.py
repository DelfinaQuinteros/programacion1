from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClientesModels

CLIENTES = {
    1: {'firstname': 'Pedro', 'lastname': 'Marco'},
    2: {'firstname': 'María', 'lastname': 'Sosa'},
}


class Clientes(Resource):
    """
    def get(self):
        return CLIENTES

    def post(self):
        cliente = request.get_json()
        id = int(max(CLIENTES.keys())) + 1
        CLIENTES[id] = cliente
        return CLIENTES[id], 201
    """

    def get(self):
        clientes = db.session.query(ClientesModels).all()
        return jsonify([clientes.to_json() for cliente in clientes])

    def post(self):
        cliente = ClientesModels.from_json(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201


class Cliente(Resource):
    """
    def get(self, id):
        if int(id) in CLIENTES:
            return CLIENTES[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in CLIENTES:
            del CLIENTES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in CLIENTES:
            cliente = CLIENTES[int(id)]
            date = request.get_json()
            cliente.update(date)
            return cliente, 201
        return '', 404
    """

    def get(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        return cliente.to_json()

    def delete(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204

    def put(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201
