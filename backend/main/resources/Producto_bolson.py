from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoBolsonModels


class ProductosBolsones(Resource):
    def get(self):
        page = 1
        per_page = 10
        productosbolsones = db.session.query(ProductoBolsonModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        productobolsones = productosbolsones.paginate(page, per_page, True, 30)
        return jsonify({'productosbolsones': [productobolson.to_json() for productobolson in productosbolsones],
                        'total': productobolsones.total,
                        'page': productobolsones.page,
                        'pages': productobolsones.pages
                        })

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
