from .. import db


class Compras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    retirado = db.Column(db.Boolean, nullable=False)
    fechaCompra = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Compras: %r %r >' % (self.retirado, self.fechaCompra)

    def to_json(self):
        compras_json = {
            'id': self.id,
            'retirado': str(self.retirado),
            'fechaCompra': str(self.fechaCompra),
        }
        return compras_json

    def from_json(compras_json):
        id = compras_json.get('id')
        retirado = compras_json.get('retirado')
        fechaCompra = compras_json.get('fechaCompra')
        return Compras(id=id,
                       retirado=retirado,
                       fechaCompra=fechaCompra,
                       )
