from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels


class Bolsones(Resource):
    def get(self):
        bolsones = db.session.query(BolsonesModels).all()
        bolsonespendientes = db.session.query(BolsonesModels).filter(BolsonesModels.aprobado == 0).all()
        bolsonesprevios = db.session.query(BolsonesModels).filter(BolsonesModels.aprobado == 1).all()
        return jsonify([bolson.to_json() for bolson in bolsones])


class Bolson(Resource):
    def get(self, id):
        bolson = db.session.query(BolsonesModels).get_or_404(id)
        return bolson.to_json()
