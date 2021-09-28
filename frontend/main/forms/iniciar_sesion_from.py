from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class Inicio_Sesion_Form(FlaskForm):
    email = EmailField('E-mail',
                       [
                           validators.Required(message="E-mail es obligatorio"),
                           validators.Email(message='Formato invalido'),
                       ])

    password = PasswordField('Password', [
        validators.Required(message='Password es obligatorio'),
    ])

    submit = SubmitField("Send")
