from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClienteModels


class Clientes(Resource):
    def get(self):
        clientes = db.session.query(ClienteModels).all()
        return jsonify([cliente.to_json() for cliente in clientes])

    def post(self):
        cliente = ClienteModels.from_json(request.get_json())
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente.to_json(), 201
        except:
            return '', 404


class Cliente(Resource):
    def get(self, id):
        cliente = db.session.query(ClienteModels).get_or_404(id)
        return cliente.to_json()

    def delete(self, id):
        cliente = db.session.query(ClienteModels).get_or_404(id)
        try:
            db.session.delete(cliente)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        cliente = db.session.query(ClienteModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente.to_json(), 201
        except:
            return '', 404
