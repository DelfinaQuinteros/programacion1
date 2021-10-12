import json
import requests
from flask import Blueprint, render_template

from ..forms.registrarse_from import Registrarse_Form

# Crear Blueprint
registrarse = Blueprint('registrarse', __name__, url_prefix='/registrarse')


@registrarse.route('/')
def index():
    return render_template('registrarse.html')


@registrarse.route('/create', methods=["POST", "GET"])
def create():
    form = Registrarse_Form()
    if form.validate_on_submit():
        data = {}
        data["nombre"] = form.firstname.data
        data["apellido"] = form.lastname.data
        data["E-mail"] = form.email.data
        data["password"] = form.password.data
        data["Confirm"] = form.password.data

        print(data)
        headers = {
            'content-type': "application/json"
        }
        r = requests.post(
            current_app.config["API_URL"] + '/registrarse',
            headers=headers,
            data=json.dumps(data))
        return redirect(url_for('registrarse.html'))
    return render_template('registrarse.html', form=form)


@registrarse.route('/inicio/<int:id>')
def inicio(id):
    return render_template('inicio.html')


@registrarse.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')
