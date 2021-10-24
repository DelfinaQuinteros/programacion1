from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class CompraForms:
    bolsonId = IntergerField(label=None)
    send = SubmitField("Comprar")
