from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels

BOLSONES = {
    1: {'primer bolson': 'Bolson1'},
    2: {'segundo bolson': 'Bolson2'},
    3: {'tercer bolson': 'Bolson3'},
}


class Bolsones(Resource):
    """
    def get(self):
        return BOLSONES
    """
    def get(self):
        bolsones = db.session.query(BolsonesModels).all()
        return jsonify([bolsones.to_json() for bolson in bolsones])


class Bolson(Resource):
    """
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return "", 404
    """
    def get(self, id):
        bolson = db.session.query(BolsonesModels).get_or_404(id)
        return bolson.to_json()
