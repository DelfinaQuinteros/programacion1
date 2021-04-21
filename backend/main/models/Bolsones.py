from .. import db


class Bolsones(db.Model):
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
        return Bolsones(id=id,
                        nombre=nombre,
                        aprobado=aprobado,
                        fecha=fecha,
                        )


"""
en to_json
self.bolsones = db.session.query(BolsonesModels).get_or_404(self.bolsonesId)
'bolsones' =  self.bolson.to_json
bolsonesId = db.Column(db.Integrer, db.Foreignkey('BolsonesId'))
bolsones = db.relationship("nombre de la clase con la que se relacion", back_populates="nombre de lo que se relaciona", uselist=False)
"""