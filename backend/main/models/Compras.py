from .. import db
from datetime import datetime

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates='compras', uselist=False, single_parent=True)
    usuario = db.relationship('Usuario', back_populates='compras', uselist=False, single_parent=True)

    def __repr__(self):
        return '<Compra: %r %r %r %r >' % (self.fechacompra, self.retirado, self.usuario, self.bolson)

    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra.strftime('%Y-%m-%d'),
            'retirado': str(self.retirado),
            'bolson': self.bolson.to_json(),
            'usuario': self.usuario.to_json(),
        }
        return compra_json

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fechacompra = datetime.strptime(compra_json.get('fechacompra'), '%Y-%m-%d')
        retirado = compra_json.get('retirado')
        bolsonid = compra_json.get('bolsonid')
        usuarioid = compra_json.get('usuarioid')
        return Compra(id=id,
                      fechacompra=fechacompra,
                      retirado=retirado,
                      bolsonid=bolsonid,
                      usuarioid=usuarioid,
                      )
