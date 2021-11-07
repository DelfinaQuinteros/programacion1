from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModels
from main.auth.Decorators import admin_or_cliente_required


class Bolsones(Resource):
    #@admin_or_cliente_required
    def get(self):
        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        bolsones = bolsones.paginate(page, per_page, True, 30)
        return jsonify({'bolsones': [bolson.to_json() for bolson in bolsones.items],
                        'total': bolsones.total,
                        'page': bolsones.page,
                        'pages': bolsones.pages
                        })


class Bolson(Resource):
    #@admin_or_cliente_required
    def get(self, id):
        bolson = db.session.query(BolsonModels).get_or_404(id)
        return bolson.to_json()
