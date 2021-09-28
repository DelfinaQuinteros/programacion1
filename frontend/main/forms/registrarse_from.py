from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class Registrarse_Form(FlaskForm):
    firstname = StringField('Nombre',
                            [
                                validators.Required(message="El nombre es obligatorio"),
                            ])

    lastname = StringField('Apellido',
                           [
                               validators.Required(message="El apellido es obligatorio"),
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

    submit = SubmitField("Send")
