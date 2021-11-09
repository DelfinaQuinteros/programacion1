from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class AgregarProductoForms:
    nombre = StringField('Nombre',
                            [
                                validators.Required(message="El nombre del producto obligatorio"),
                            ])
    submit = SubmitField("Agregar producto")


class ModificarProductoForms:
    nombre = StringField('Nombre',
                            [
                                validators.Required(message="El nombre del producto obligatorio"),
                            ])
    submit = SubmitField("Modificar producto")


class EliminarProductoForms:
    nombre = StringField('Nombre',
                            [
                                validators.Required(message="El nombre del producto obligatorio"),
                            ])
    submit = SubmitField("Eliminar producto")
