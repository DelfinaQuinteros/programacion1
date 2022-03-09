from .. import db
import datetime as dt
from . import Producto_bolson


class Bolson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    aprobado = db.Column(db.Boolean, default=False, nullable=False)
    fecha = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    compras = db.relationship('Compra', back_populates='bolson', cascade="all, delete-orphan")
    productosbolsones = db.relationship("ProductoBolson", back_populates="bolson", cascade="all, delete-orphan")

    def _repr_(self):
        return '<Bolson: %r %r %r %r %r %r >' % (self.nombre, self.aprobado, self.fecha, self.descripcion, self.precio, self.productosbolsones)

    def to_json(self):
        productosbolsones = []
        print('NO ENTRA', self.productosbolsones)
        if self.productosbolsones:
            print('entra', self.productosbolsones)
            for producto in self.productosbolsones:
                productosbolsones.append(producto.to_json())
        bolson_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'aprobado': self.aprobado,
            'fecha': str(self.fecha),
            'descripcion': self.descripcion,
            'precio': self.precio,
            'productosbolsones': productosbolsones,
        }
        return bolson_json

    @staticmethod
    def from_json(bolson_json):
        id = bolson_json.get('id')
        nombre = bolson_json.get('nombre')
        fecha = bolson_json.get('fecha')
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
        if 'productosbolsones' in bolson_json:
            for productoId in bolson_json.get('productosbolsones'):
                bolson.productosbolsones.append(Producto_bolson.ProductoBolson(productoId=productoId))
        print(bolson)
        return bolson
