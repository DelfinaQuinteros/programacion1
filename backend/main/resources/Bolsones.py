from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModels


class Bolsones(Resource):
    def get(self):
        bolsones = db.session.query(BolsonModels).all()
        bolsonespendientes = db.session.query(BolsonModels).filter(BolsonModels.aprobado == 0).all()
        bolsonesprevios = db.session.query(BolsonModels).filter(BolsonModels.aprobado == 1).all()
        return jsonify([bolson.to_json() for bolson in bolsones])


class Bolson(Resource):
    def get(self, id):
        bolson = db.session.query(BolsonModels).get_or_404(id)
        return bolson.to_json()
