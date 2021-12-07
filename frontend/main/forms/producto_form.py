from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, StringField, SelectMultipleField, FloatField, IntegerField, DateTimeField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired
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


class FormFilterProducto(FlaskForm):
    """    proveedorid = SelectField('', [validators.optional()], coerce=int)
    ordenamiento = SelectField('',
                               choices=[('producto', "Producto"), ('proveedor', "Proveedor")],
                               validators=[InputRequired()], coerce=str, default='producto')"""
    proveedor = SelectField('', [validators.Required(message='Campo Requerido')],
                            coerce=int)
    submit = SubmitField("Filtrar")
