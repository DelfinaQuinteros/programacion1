from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, StringField, SelectMultipleField, FloatField, IntegerField, DateTimeField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired
from wtforms import validators


class BolsonForms(FlaskForm):
    nombre = StringField('Nombre:',
                         [
                             validators.Required(message="El nombre es obligatorio"),
                         ],
                         render_kw={"placeholder": "Nombre del bolson"}
                         )
    aprobado = IntegerField('Aprobar:',
                            [
                                validators.Required(message="Es obligatorio aprobar el bolson"),
                            ],
                            render_kw={"placeholder": "Ingrese '1'"}
                            )
    fecha = StringField("Fecha:",
                        [
                            validators.Required(message="La fecha es obligatoria")
                        ],
                        render_kw={"placeholder": "%Y-%m-%d"}
                        )
    descripcion = StringField("Descripcion",
                              [
                                  validators.Required(message="La descripcion es obligatoria")
                              ],
                              render_kw={"placeholder": "Descripcion"}
                              )
    producto = SelectField(
        'Seleccionar producto #1',
        [validators.Required(message='Este campo es obligatorio')], coerce=int,
        render_kw={"placeholder": "Producto #1"}
    )
    producto2 = SelectField(
        'Seleccionar producto #2', coerce=int,
        render_kw={"placeholder": "Producto #2"}
    )
    producto3 = SelectField(
        'Seleccionar producto #3', coerce=int,
        render_kw={"placeholder": "Producto #3"}
    )
    producto4 = SelectField(
        'Seleccionar producto #4', coerce=int,
        render_kw={"placeholder": "Producto #4"}
    )
    producto5 = SelectField(
        'Seleccionar producto #5', coerce=int,
        render_kw={"placeholder": "Producto #5"}
    )

    precio = FloatField("Precio:",
                        [
                            validators.Required(message="El precio es obligatorio")
                        ],
                        render_kw={"placeholder": "$0000"})
    productosId = SelectMultipleField("", coerce=int)
    submit = SubmitField("Agregar bolson")


class FormFilterBolson(FlaskForm):
    nombre = StringField('', [validators.optional()])
    desde = FloatField('', [validators.optional()])
    hasta = FloatField('', [validators.optional()])
    ordenamiento = SelectField('',
                               choices=[('fecha', "Fecha"), ('asc', "Precio ascendente"), ('desc', "Precio descendente")],
                               validators=[InputRequired()], coerce=str, default='fecha'
                               )
    submit = SubmitField('Filtrar')


class FormFilterBolsones(FlaskForm):
    desde = DateTimeField('', [validators.optional()], format='%Y-%m-%d')
    hasta = DateTimeField('', [validators.optional()], format='%Y-%m-%d')
    submit = SubmitField('Filtrar')
