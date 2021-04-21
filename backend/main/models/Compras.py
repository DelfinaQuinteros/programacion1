from .. import db
from datetime import datetime


class Compras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<Compras: %r %r >' % (self.fechacompra, self.retirado)

    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra.strftime('%y-%m-%d').date(),
            'retirado': self.retirado
        }

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fechacompra = datetime.strptime(compra_json.get('fechacompra'), '%y-%m-%d').date()
        retirado = compra_json.get('retirado')
        return Compras(
            id=id,
            fechacompra=fechacompra,
            retirado=retirado
        )
