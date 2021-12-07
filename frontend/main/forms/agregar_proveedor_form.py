from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, StringField, SelectMultipleField, PasswordField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired
from wtforms import validators


class AgregarProveedorForm(FlaskForm):
    nombre = StringField('Nombre:',
                         [
                             validators.Required(message="El nombre es obligatorio"),
                         ],
                         render_kw={"placeholder": "Nombre"})

    apellido = StringField('Apellido:',
                           [
                               validators.Required(message="El apellido es obligatorio"),
                           ],
                           render_kw={"placeholder": "Apellido"})

    telefono = StringField("Telefono:",
                           [
                               validators.Required(message="El telefono es obligatorio")
                           ],
                           render_kw={"placeholder": "Telefono"})

    email = EmailField('Email:',
                       [
                           validators.Required(message="El email es obligatorio"),
                           validators.Email(message='Formato no valido'),
                       ],
                       render_kw={"placeholder": "Email"})

    password = PasswordField('Contraseña:', [
        validators.Required(),
        validators.EqualTo('confirm', message='Las contraseñas no coinciden')
    ],
                             render_kw={"placeholder": "Contraseña"})

    confirm = PasswordField('Repita la contraseña:',
                            render_kw={"placeholder": "Repita la contraseña"})

    submit = SubmitField("Agregar proveedor")


class FormFilterProveedor(FlaskForm):
    ordenamiento = SelectField('',
                               choices=[('nombre', "Nombre"), ('apellido', "Apellido")],
                               validators=[InputRequired()], coerce=str, default='nombre')
    submit = SubmitField("Ordenar")
