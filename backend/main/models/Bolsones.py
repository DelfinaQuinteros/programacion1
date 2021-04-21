from .. import db


class Bolson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    aprobado = db.Column(db.Boolean, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Bolson: %r %r %r >' % (self.nombre, self.aprobado, self.fecha)

    def to_json(self):
        bolsones_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'aprobado': str(self.aprobado),
            'fecha': str(self.fecha)

        }
        return bolsones_json

    @staticmethod
    def from_json(bolsones_json):
        id = bolsones_json.get('id')
        nombre = bolsones_json.get('nombre')
        aprobado = bolsones_json.get('aprobado')
        fecha = bolsones_json.get('fecha')
        return Bolson(id=id,
                        nombre=nombre,
                        aprobado=aprobado,
                        fecha=fecha,
                        )


