from .. import db
from datetime import datetime


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)
    bolsonid= db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    clienteid= db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates='compras', uselist=False, single_parent=True)
    cliente= db.relationship('Cliente', back_populates='compras', uselist=False, single_parent=True)

    def __repr__(self):
        return '<Compra: %r %r %r %r >' % (self.fechacompra, self.retirado, self.cliente.to_json(), self.bolson.to_json())

    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra.strftime('%Y-%m-%d'),
            'retirado': str(self.retirado),
            'bolson': self.bolson.to_json(),
            'cliente': self.cliente.to_json()
        }
        return compra_json

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fechacompra = datetime.strptime(compra_json.get('fechacompra'), '%Y-%m-%d')
        retirado = compra_json.get('retirado')
        bolsonid = compra_json.get('bolsonid')
        clienteid = compra_json.get('clienteid')
        return Compra(id=id,
                      fechacompra=fechacompra,
                      retirado=retirado,
                      bolsonid=bolsonid,
                      clienteid=clienteid
                      )
