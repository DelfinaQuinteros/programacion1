from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, StringField, SelectMultipleField, FloatField, IntegerField, DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class BolsonForms(FlaskForm):
    id = IntegerField('Id:',
                      [validators.Required(message="El id es obligatorio")],
                      render_kw={"placeholder": "Id del bolson"}
                      )
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
                        ],  # format='%Y-%m-%d',
                        render_kw={"placeholder": "%Y-%m-%d"}
                        )
    descripcion = StringField("Descripcion",
                              [
                                  validators.Required(message="La descripcion es obligatoria")
                              ],
                              render_kw={"placeholder": "Descripcion"}
                              )
    precio = FloatField("Precio:",
                        [
                            validators.Required(message="El precio es obligatorio")
                        ],
                        render_kw={"placeholder": "$0000"})
    productosId = SelectMultipleField("", coerce=int)
    submit = SubmitField("Agregar bolson")


class FormFilterBolsones(FlaskForm):
    desde = DateTimeField('', [validators.optional()], format='%Y-%m-%d')
    hasta = DateTimeField('', [validators.optional()], format='%Y-%m-%d')
    submit = SubmitField('Filtrar')
