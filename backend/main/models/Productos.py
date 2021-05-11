from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import usuarioModels
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.Decorators import admin_required


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates='productos', uselist=False, single_parent=True)
    productosbolsones = db.relationship("ProductoBolson", back_populates="producto", cascade="all, delete-orphan")

    def __repr__(self):
        return '<Productos: %r  >' % self.nombre

    def to_json(self):
        productos_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'usuario': self.usuario.nombre
        }
        return productos_json

    @staticmethod
    def from_json(productos_json):
        id = productos_json.get('id')
        nombre = productos_json.get('nombre')
        usuarioid = productos_json.get('usuarioid')
        return Producto(id=id,
                        nombre=nombre,
                        usuarioid=usuarioid
                        )

