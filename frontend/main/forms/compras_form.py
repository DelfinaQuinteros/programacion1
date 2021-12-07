from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, StringField, SelectMultipleField, SelectField
from wtforms.validators import InputRequired
from wtforms import validators


class FormFilterCompras(FlaskForm):
    nombre = StringField('', [validators.optional()])
    apellido = StringField('', [validators.optional()])
    retirado = SelectField('', [validators.optional()], choices=[(2, "Retirado"), (1, "Si"), (0, "No")], coerce=int, default=2)
    ordenamiento = SelectField('',
                               choices=[('id', "N° de Compra"), ('fecha', "Fecha compra"), ('nombre', "Nombre cliente"),
                                        ('apellido', "Apellido cliente")],
                               validators=[InputRequired()], coerce=str, default=id)
    submit = SubmitField("Filtrar-Ordenar")