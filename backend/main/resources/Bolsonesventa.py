from flask_restful import Resource
from flask import request, jsonify
from datetime import datetime, timedelta
from .. import db
from main.models import BolsonModels


class BolsonesVenta(Resource):
    def get(self):
        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        bolsones = bolsones.paginate(page, per_page, True, 30)
        return jsonify({'bolsonesventa': [bolson.to_json() for bolson in bolsones.items if bolson.aprobado == 1],
                        'total': bolsones.total,
                        'page': bolsones.page,
                        'pages': bolsones.pages
                        })

    
class BolsonVenta(Resource):
    def get(self, id):
        bolsonventa = db.session.query(BolsonModels).get_or_404(id)
        if bolsonventa.aprobado == 1:
            return bolsonventa.to_json()
        else:
            return '', 404
