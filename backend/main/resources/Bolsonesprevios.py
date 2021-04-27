from flask_restful import Resource
from flask import request
from datetime import datetime, timedelta
from .. import db
from main.models import BolsonModels


class BolsonesPrevios(Resource):
    def get(self):
        fecha = datetime.today() - timedelta(days=7)
        bolsonesprevios = db.session.query(BolsonModels).filter(BolsonModels.fecha <= fecha).all
        return bolsonesprevios


class BolsonPrevio(Resource):
    def get(self, id):
        if int(id) in bolsonesprevios:
            return bolsonesprevios[int(id)]
        return "", 404
