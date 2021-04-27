from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoBolsonModels


class ProductosBolsones(Resource):
    def get(self):
        productosbolsones = db.session.query(ProductoBolsonModels).all()
        return jsonify({'productosbolsones': [productobolson.to_json() for productobolson in productosbolsones]})

    def post(self):
        productobolson = ProductoBolsonModels.from_json(request.get_json())
        try:
            db.session.add(productobolson)
            db.session.commit()
            return productobolson.to_json(), 201
        except:
            return '', 404


class ProductoBolson(Resource):
    def get(self, id):
        productobolson = db.session.query(ProductoBolsonModels).get_or_404(id)
        try:
            return productobolson.to_json()
        except:
            return '', 404

    def delete(self, id):
        productobolson = db.session.query(ProductoBolsonModels).get_or_404(id)
        try:
            db.session.delete(productobolson)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        productobolson = db.session.query(ProductoBolsonModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(productobolson, key, value)
        try:
            db.session.add(productobolson)
            db.session.commit()
            return productobolson.to_json(), 201
        except:
            return '', 404
