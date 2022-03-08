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
    submit = SubmitField("Agregar producto")


class FormFilterProducto(FlaskForm):
    proveedor = SelectField('', [validators.Required(message='Campo Requerido')],
                            coerce=int)
    submit = SubmitField("Filtrar")
