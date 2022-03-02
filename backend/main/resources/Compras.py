from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import CompraModels, BolsonModels
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.Decorators import admin_required
from main.auth.Decorators import admin_or_cliente_required


class Compras(Resource):
    # @admin_required
    def get(self):
        page = 1
        per_page = 10
        compras = db.session.query(CompraModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        compras = compras.paginate(page, per_page, True, 30)
        return jsonify({'clientes': [compra.to_json() for compra in compras.items],
                        'total': compras.total,
                        'page': compras.page,
                        'pages': compras.pages
                        })

    @admin_or_cliente_required
    def post(self):
        compra = CompraModels.from_json(request.get_json())
        current_user = get_jwt_identity()
        compra.usuarioId = current_user
        try:
            db.session.add(compra)
            db.session.commit()
        except Exception:
            return 'Formato no correcto', 400
        return compra.to_json(), 201


class Compra(Resource):
    @admin_or_cliente_required
    def get(self, id):
        compra = db.session.query(CompraModels).get_or_404(id)
        return compra.to_json()

    @admin_or_cliente_required
    def delete(self, id):
        compra = db.session.query(CompraModels).get_or_404(id)
        try:
            db.session.delete(compra)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    @admin_required
    def put(self, id):
        compra = db.session.query(CompraModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra, key, value)
        try:
            db.session.add(compra)
            db.session.commit()
            return compra.to_json(), 201
        except:
            return '', 404
