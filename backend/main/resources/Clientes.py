from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModels
from main.auth.Decorators import admin_required
from flask_jwt_extended import jwt_required


class Clientes(Resource):
    #@jwt_required()
    def get(self):
        page = 1
        per_page = 10
        clientes = db.session.query(UsuarioModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        clientes = clientes.paginate(page, per_page, True, 30)
        return jsonify({'clientes': [cliente.to_json() for cliente in clientes.items],
                        'total': clientes.total,
                        'page': clientes.page,
                        'pages': clientes.pages
                        })

    #@jwt_required()
    def post(self):
        cliente = UsuarioModels.from_json(request.get_json())
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente.to_json(), 201
        except:
            return '', 404


class Cliente(Resource):
    #@jwt_required()
    def get(self, id):
        cliente = db.session.query(UsuarioModels).get_or_404(id)
        return cliente.to_json()

    #@admin_required
    def delete(self, id):
        cliente = db.session.query(UsuarioModels).get_or_404(id)
        try:
            db.session.delete(cliente)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    #@jwt_required()
    def put(self, id):
        cliente = db.session.query(UsuarioModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente.to_json(), 201
        except:
            return '', 404
