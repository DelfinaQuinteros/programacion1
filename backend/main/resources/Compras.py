from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ComprasModels


class Compras(Resource):
    def get(self):
        compras = db.session.query(ComprasModels).all()
        return jsonify([compra.to_json() for compra in compras])

    def post(self):
        compra = ComprasModels.from_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201


class Compra(Resource):
    def get(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        return compra.to_json()

    def delete(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        db.session.delete(compra)
        db.session.commit()
        return '', 204

    def put(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra, key, value)
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201
