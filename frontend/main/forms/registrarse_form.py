from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class RegistrarseForm(FlaskForm):
    nombre = StringField('Nombre',
                            [
                                validators.Required(message="El nombre es obligatorio"),
                            ])

    apellido = StringField('Apellido',
                           [
                               validators.Required(message="El apellido es obligatorio"),
                           ])

    telefono = StringField("Telefono",
                             [
                                 validators.Required(message="El telefono es obligatorio")
                             ])

    email = EmailField('E-mail',
                       [
                           validators.Required(message="El E-mail es obligatorio"),
                           validators.Email(message='Formato no valido'),
                       ])

    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Las contraseñas no coinciden')
    ])

    confirm = PasswordField('Repita la contraseña')

    submit = SubmitField("Registrarse")
