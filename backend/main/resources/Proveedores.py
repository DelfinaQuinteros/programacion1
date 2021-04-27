from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProveedorModels


class Proveedores(Resource):
    def get(self):
        proveedores = db.session.query(ProveedorModels).all()
        return jsonify([proveedor.to_json() for proveedor in proveedores])

    def post(self):
        proveedor = ProveedorModels.from_json(request.get_json())
        try:
            db.session.add(proveedor)
            db.session.commit()
            return proveedor.to_json(), 201
        except:
            return '', 404


class Proveedor(Resource):
    def get(self, id):
        proveedor = db.session.query(ProveedorModels).get_or_404(id)
        return proveedor.to_json()

    def delete(self, id):
        proveedor = db.session.query(ProveedorModels).get_or_404(id)
        try:
            db.session.delete(proveedor)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        proveedor = db.session.query(ProveedorModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(proveedor, key, value)
        try:
            db.session.add(proveedor)
            db.session.commit()
            return proveedor.to_json(), 201
        except:
            return '', 404