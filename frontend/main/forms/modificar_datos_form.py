from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class ModificarDatosForm(FlaskForm):
    nombre = StringField('Nombre',
                         [
                             validators.Required(message="El nombre es obligatorio"),
                         ],
                         render_kw={"placeholder": "Nombre"}
                         )

    apellido = StringField('Apellido',
                           [
                               validators.Required(message="El apellido es obligatorio"),
                           ],
                           render_kw={"placeholder": "Apellido"}
                           )

    telefono = IntegerField("Telefono",
                            [
                                validators.Required(message="El telefono es obligatorio")
                            ],
                            render_kw={"placeholder": "Telefono"}
                            )

    password = PasswordField('Contraseña', [
        validators.Required(message="La contraseña es obligatoria")
    ],
                             render_kw={"placeholder": "Contraseña"})

    submit = SubmitField("Actualizar datos")
