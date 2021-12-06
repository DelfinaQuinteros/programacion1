from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoModels
from main.auth.Decorators import admin_or_proveedor_required
from flask_jwt_extended import jwt_required


class Productos(Resource):
    @admin_or_proveedor_required
    def get(self):
        page = 1
        per_page = 10
        iduser = get_jwt_identity
        user = db.session.query(UsuarioModels).get_or_404(iduser)
        if user.role == 'admin':
            productos = db.session.query(ProductoModels)
        if user.role == 'proveedor':
            productos = db.session.query(ProductoModels).filter(ProductoModels.proveedorid == iduser)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == 'proveedorid':
                    productos = productos.filter(ProductoModels.proveedorid == value)
                if key == 'ordenamiento':
                    if value == 'productos':
                        productos = productos.order_by(ProductoModels.nombre.asc())
                    if value == 'proveedor':
                        productos = productos.join(UsuarioModels, ProductoModels.proveedor).order_by(UsuarioModels.nombre.asc())
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        productos = productos.paginate(page, per_page, True, 30)
        return jsonify({'productos': [producto.to_json() for producto in productos.items],
                        'total': productos.total,
                        'page': productos.page,
                        'pages': productos.pages
                        })

    @admin_or_proveedor_required
    def post(self):
        producto = ProductoModels.from_json(request.get_json())
        try:
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(), 201
        except:
            return '', 404


class Producto(Resource):
    @jwt_required()
    def get(self, id):
        producto = db.session.query(ProductoModels).get_or_404(id)
        return producto.to_json()

    @admin_or_proveedor_required
    def delete(self, id):
        producto = db.session.query(ProductoModels).get_or_404(id)
        try:
            db.session.delete(producto)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    @admin_or_proveedor_required
    def put(self, id):
        producto = db.session.query(ProductoModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        try:
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(), 201
        except:
            return '', 404
