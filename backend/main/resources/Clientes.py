from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClientesModels


class Clientes(Resource):
    def get(self):
        clientes = db.session.query(ClientesModels).all()
        return jsonify([cliente.to_json() for cliente in clientes])

    def post(self):
        cliente = ClientesModels.from_json(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201


class Cliente(Resource):
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