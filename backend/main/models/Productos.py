from .. import db


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    proveedorid = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    proveedor = db.relationship('Proveedor', back_populates='productos', uselist=False, single_parent=True)

    def __repr__(self):
        return '<Productos: %r  >' % self.nombre

    def to_json(self):
        productos_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'proveedor': self.proveedor.nombre
        }
        return productos_json

    @staticmethod
    def from_json(productos_json):
        id = productos_json.get('id')
        nombre = productos_json.get('nombre')
        proveedorid = productos_json.get('proveedorid')
        return Producto(id=id,
                        nombre=nombre,
                        proveedorid=proveedorid
                        )
