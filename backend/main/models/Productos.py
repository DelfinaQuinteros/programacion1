from .. import db


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Productos: %r  >' % self.nombre

    def to_json(self):
        productos_json = {
            'id': self.id,
            'nombre': str(self.nombre),
        }
        return productos_json

    @staticmethod
    def from_json(productos_json):
        id = productos_json.get('id')
        nombre = productos_json.get('nombre')
        return Productos(id=id,
                         nombre=nombre,
                         )
