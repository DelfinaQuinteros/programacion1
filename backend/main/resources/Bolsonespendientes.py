from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModels


class BolsonesPendientes(Resource):
    def get(self):
        page = 1
        per_page = 10
        bolsonespendientes = db.session.query(BolsonModels).filter(BolsonModels.aprobado == 0).all()
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        bolsones = bolsonespendientes.paginate(page, per_page, True, 30)
        return jsonify({'bolsonespendientes': [bolson.to_json() for bolson in bolsones.items],
                        'total': bolsones.total,
                        'page': bolsones.page,
                        'pages': bolsones.pages
                        })

    def post(self):
        bolsonpendiente = BolsonModels.from_json(request.get_json())
        try:
            db.session.add(bolsonpendiente)
            db.session.commit()
            return bolsonpendiente.to_json(), 201
        except:
            return '', 404


    def get(self):

        bolsones = db.session.query(BolsonModels)



class BolsonPendiente(Resource):
    def get(self, id):
        bolsonpendiente = db.session.query(BolsonModels).get_or_404(id)
        return bolsonpendiente.to_json()

    def delete(self, id):
        bolsonpendiente = db.session.query(BolsonModels).get_or_404(id)
        try:
            db.session.delete(bolsonpendiente)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        bolsonpendiente = db.session.query(BolsonModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(bolsonpendiente, key, value)
        try:
            db.session.add(bolsonpendiente)
            db.session.commit()
            return bolsonpendiente.to_json(), 201
        except:
            return '', 404
