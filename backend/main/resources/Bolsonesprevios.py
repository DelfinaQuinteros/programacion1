from flask_restful import Resource
from flask import request, jsonify
from datetime import datetime, timedelta
from .. import db
from main.models import BolsonModels
from main.auth.Decorators import admin_required


class BolsonesPrevios(Resource):
    fecha = datetime.today() - timedelta(days=7)

    #@admin_required
    def get(self):
        page = 1
        per_page = 10
        bolsonesprevios = db.session.query(BolsonModels).filter(BolsonModels.fecha <= self.fecha)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == 'desde':
                    bolsonesprevios = bolsonesprevios.filter(BolsonModels.fecha >= value)
                if key == 'hasta':
                    bolsonesprevios = bolsonesprevios.filter(BolsonModels.fecha <= value)
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        bolsones = bolsonesprevios.paginate(page, per_page, True, 30)
        return jsonify({'bolsonesprevios': [bolson.to_json() for bolson in bolsones.items],
                        'total': bolsones.total,
                        'page': bolsones.page,
                        'pages': bolsones.pages
                        })


class BolsonPrevio(Resource):
    #@admin_required
    def get(self, id):
        bolsonprevio = db.session.query(BolsonModels).get_or_404(id)
        if bolsonprevio.fecha <= BolsonesPrevios.fecha:
            return jsonify(bolsonprevio.to_json())
        else:
            return '', 404
