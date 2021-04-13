from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProveedoresModels

PROVEEDORES = {
    1: {'firstname': 'aa', 'lastname': 'bb'},
    2: {'firstname': 'cc', 'lastname': 'dd'},
}


class Proveedores(Resource):
    """
    def get(self):
        return PROVEEDORES

    def post(self):
        proveedor = request.get_json()
        id = int(max(PROVEEDORES.keys())) + 1
        PROVEEDORES[id] = proveedor
        return PROVEEDORES[int(id)], 201
    """

    def get(self):
        proveedores = db.session.query(ProveedoresModels).all()
        return jsonify([proveedores.to_json() for proveedor in proveedores])

    def post(self):
        proveedor = ProveedoresModels.from_json(request.get_json())
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json(), 201


class Proveedor(Resource):
    """
    def get(self, id):
        if int(id) in PROVEEDORES:
            return PROVEEDORES[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in PROVEEDORES:
            del PROVEEDORES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in PROVEEDORES:
            proveedor = PROVEEDORES[int(id)]
            date = request.get_json()
            proveedor.update(date)
            return proveedor, 201
        return '', 404
    """

    def get(self, id):
        proveedor = db.session.query(ProveedoresModels).get_or_404(id)
        return proveedor.to_json()

    def delete(self, id):
        proveedor = db.session.query(ProveedoresModels).get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return '', 204

    def put(self, id):
        proveedor = db.session.query(ProveedoresModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(proveedor, key, value)
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json(), 201
