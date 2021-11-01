from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class ModificarDatosForm(FlaskForm):
    firstname = StringField('Nombre',
                            [
                                validators.Required(message="El nombre es obligatorio"),
                            ])

    lastname = StringField('Apellido',
                           [
                               validators.Required(message="El apellido es obligatorio"),
                           ])

    telefono = StringField("Telefono",
                             [
                                 validators.Required(message="El telefono es obligatorio")
                             ])

    email = EmailField('Email',
                       [
                           validators.Required(message="El Email es obligatorio"),
                           validators.Email(message='Formato no valido'),
                       ])

    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Las contraseñas no coinciden')
    ])

    confirm = PasswordField('Repita la contraseña')

    submit = SubmitField("Modificar datos")
