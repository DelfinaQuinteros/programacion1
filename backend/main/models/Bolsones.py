from .. import db
from datetime import datetime


class Bolson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    aprobado = db.Column(db.Boolean, default=False, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    compras = db.relationship('Compra', back_populates='bolson', cascade="all, delete-orphan")
    productosbolsones = db.relationship("ProductoBolson", back_populates="bolson", cascade="all, delete-orphan")

    def _repr_(self):
        return '<Bolson: %r %r %r %r %r >' % (self.nombre, self.aprobado, self.fecha, self.descripcion, self.precio)

    def to_json(self):
        bolson_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'aprobado': self.aprobado,
            'fecha': self.fecha.strftime('%Y-%m-%d'),
            'producto': self.productosbolsones,
            'descripcion': self.descripcion,
            'precio': self.precio
        }
        return bolson_json

    @staticmethod
    def from_json(bolson_json):
        id = bolson_json.get('id')
        nombre = bolson_json.get('nombre')
        fecha = datetime.strptime(bolson_json.get('fecha'), '%Y-%m-%d')
        aprobado = bolson_json.get('aprobado')
        descripcion = bolson_json.get('descripcion')
        precio = bolson_json.get('precio')
        bolson = Bolson(id=id,
                        nombre=nombre,
                        aprobado=aprobado,
                        fecha=fecha,
                        descripcion=descripcion,
                        precio=precio
                        )
        if 'producto' in bolson_json:
            for productoId in bolson_json.get('producto'):
                bolson.productosbolsones.append(ProductoBolsonModels(productoId=productoId))
        return bolson
