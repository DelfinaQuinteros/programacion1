from .. import db
from datetime import datetime


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<Compras: %r %r >' % (self.fechacompra, self.retirado)

    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra.strftime('%Y-%m-%d'),
            'retirado': self.retirado
        }
        return compra_json

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fechacompra = datetime.strptime(compra_json.get('fechacompra'), '%Y-%m-%d')
        retirado = compra_json.get('retirado')
        return Compras(
            id=id,
            fechacompra=fechacompra,
            retirado=retirado
        )

"""
from .. import db
from datetime import datetime
class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)
    bolsonid= db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates='compras', uselist=False, single_parent=True)
    def _repr_(self):
        return '<Compra: %r %r >' % (self.fechacompra, self.retirado, self.bolsonid)
    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra.strftime('%Y-%m-%d'),
            'retirado': str(self.retirado),
            'bolson': self.bolson.nombre
        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        fechacompra = datetime.strptime(compra_json.get('fechacompra'), '%Y-%m-%d')
        retirado = compra_json.get('retirado')
        bolsonid= compra_json.get('bolsonid')
        return Compra(id=id,
                    fechacompra=fechacompra,
                    retirado=retirado,
                    bolsonid=bolsonid
                    )
"""
