from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class RegistrarseForm(FlaskForm):
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

    submit = SubmitField("Registrarse")
