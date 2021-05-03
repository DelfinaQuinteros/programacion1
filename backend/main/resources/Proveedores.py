from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProveedorModels


class Proveedores(Resource):
    def get(self):
        page = 1
        per_page = 10
        proveedores = db.session.query(ProveedorModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        proveedores = proveedores.paginate(page, per_page, True, 30)
        return jsonify({'productos': [proveedor.to_json() for proveedor in proveedores.items],
                        'total': proveedores.total,
                        'page': proveedores.page,
                        'pages': proveedores.pages
                        })

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