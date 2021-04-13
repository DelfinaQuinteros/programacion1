from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductosModels

PRODUCTOS = {
    1: {'primer producto': '1er producto'},
    2: {'segundo producto': '2do producto'}
}


class Productos(Resource):
    """
    def get(self):
        return PRODUCTOS

    def post(self):
        producto = request.get_json()
        id = int(max(PRODUCTOS.keys())) + 1
        PRODUCTOS[int(id)] = producto
        return PRODUCTOS[int(id)], 201
    """
    def get(self):
        productos = db.session.query(ProductosModels).all()
        return jsonify([productos.to_json() for producto in productos])

    def post(self):
        producto = ProductosModels.from_json(request.get_json())
        db.session.add(producto)
        db.session.commit()
        return producto.to_json(), 201


class Producto(Resource):
    """
    def get(self, id):
        if int(id) in PRODUCTOS:
            return PRODUCTOS[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in PRODUCTOS:
            del PRODUCTOS[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in PRODUCTOS:
            producto = PRODUCTOS[int(id)]
            date = request.get_json()
            producto.update(date)
            return producto, 201
        return '', 404
    """
    def get(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        return producto.to_json()

    def delete(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204

    def put(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        db.session.add(producto)
        db.session.commit()
        return producto.to_json(), 201
