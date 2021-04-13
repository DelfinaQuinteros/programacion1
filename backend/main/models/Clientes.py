from .. import db


class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Cliente: %r %r %r %r >' % (self.nombre, self.apellido, self.telefono, self.mail)

    def to_json(self):
        clientes_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'telefono': str(self.telefono),
            'mail': str(self.mail),
        }
        return clientes_json

    def from_json(clientes_json):
        id = clientes_json.get('id')
        nombre = clientes_json.get('nombre')
        apellido = clientes_json.get('apellido')
        telefono = clientes_json.get('telefono')
        mail = clientes_json.get('mail')
        return Clientes(id=id,
                        nombre=nombre,
                        apellido=apellido,
                        telefono=telefono,
                        mail=mail
                        )
