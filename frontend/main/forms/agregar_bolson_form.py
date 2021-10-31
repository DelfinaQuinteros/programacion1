from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class BolsonForms:
    nombre = StringField('Nombre',
                         [
                             validators.Required(message="El nombre es obligatorio"),
                         ],
                         render_kw={"placeholder": "Nombre del bolson"}
                         )
    fecha = StringField("Fecha",
                      [
                          validators.Required()
                      ], format='%Y-%m-%d'
                      )
    productosId = SelectMultipleField("", coerce=int)
    envio = SubmitField("Agregar bolson")

