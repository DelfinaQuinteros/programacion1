from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class AgregarProductoForms(FlaskForm):
    nombre = StringField('NOMBRE DEL PRODUCTO',
                         [
                             validators.Required(message="El nombre del producto obligatorio"),
                         ])
    id = IntegerField('PROVEEDOR ID',
                      [
                          validators.Required(message="El ID del proveedor obligatorio"),
                      ])
    submit = SubmitField("Agregar producto")

"""
class ModificarProductoForms:
    nombre = StringField('NOMBRE DEL PRODUCTO',
                         [
                             validators.Required(message="El nombre del producto obligatorio"),
                         ])
    submit = SubmitField("Modificar producto")


class EliminarProductoForms:
    id = IntegerField('PRODUCTO ID',
                      [
                          validators.Required(message="El ID    del producto obligatorio"),
                      ])
    submit = SubmitField("Eliminar producto")
"""