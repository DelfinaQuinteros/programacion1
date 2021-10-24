from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class ModificarDatosForm(FlaskForm):
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Las contraseñas no coinciden')
    ])

    confirm = PasswordField('Repita la contraseña')
    submit = SubmitField("Cambiar contraseña")
