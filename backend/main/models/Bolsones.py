from .. import db
from datetime import datetime


class Bolson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    aprobado = db.Column(db.Boolean, default=False, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    compras = db.relationship('Compra', back_populates='bolson', cascade="all, delete-orphan")
    productosbolsones = db.relationship("ProductoBolson", back_populates="bolson", cascade="all, delete-orphan")

    def _repr_(self):
        return '<Bolson: %r %r %r >' % (self.nombre, self.aprobado, self.fecha)

    def to_json(self):
        bolson_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'aprobado': self.aprobado,
            'fecha': self.fecha.strftime('%Y-%m-%d')
        }
        return bolson_json

    @staticmethod
    def from_json(bolson_json):
        id = bolson_json.get('id')
        nombre = bolson_json.get('nombre')
        fecha = datetime.strptime(bolson_json.get('fecha'), '%Y-%m-%d')
        aprobado = bolson_json.get('aprobado')
        return Bolson(id=id,
                      nombre=nombre,
                      aprobado=aprobado,
                      fecha=fecha
                      )
