from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModels

class BolsonesPendientes(Resource):
    def get(self):
        bolsonespendientes = db.session.query(BolsonModels).filter(BolsonModels.aprobado == 0).all()
        return jsonify([bolsonpendiente.to_json() for bolsonpendiente in bolsonespendientes])


    def post(self):
        bolsonpendiente = BolsonModels.from_json(request.get_json())
        try:
            db.session.add(bolsonpendiente)
            db.session.commit()
            return bolsonpendiente.to_json(), 201
        except:
            return '', 404


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
