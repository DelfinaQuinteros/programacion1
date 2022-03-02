from .. import db
import datetime as dt


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)
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
            'fechacompra': str(self.fechacompra),
            'retirado': str(self.retirado),
            'bolson': self.bolson.to_json(),
            'usuario': self.usuario.to_json(),
        }
        return compra_json

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fechacompra = compra_json.get('fechacompra')
        retirado = compra_json.get('retirado')
        bolsonid = compra_json.get('bolsonid')
        usuarioid = compra_json.get('usuarioid')
        return Compra(id=id,
                      fechacompra=fechacompra,
                      retirado=retirado,
                      bolsonid=bolsonid,
                      usuarioid=usuarioid,
                      )
