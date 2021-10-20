import json
import requests
from flask import Blueprint, current_app, render_template, redirect, url_for, request

# Crear Blueprint
inicio = Blueprint('inicio', __name__, url_prefix='/inicio')


@inicio.route('/')
def index():
    # Mostrar template
    return render_template('inicio.html')


@inicio.route('/iniciar_sesion/<int:id>')
def inicio_sesion(id):
    # Mostrar template
    return render_template('inicio_sesion.html')


@inicio.route('/registrarse/<int:id>')
def registrarse(id):
    # Mostrar template
    return render_template('registrarse.html')


@inicio.route('/ver-bolsones/<int:id>')
def ver_bolsones(id):
    data = {}
    data['page'] = 1
    headers = {'content-type': 'application/json'}
    print(data)
    r = requests.get(
        current_app.config["API_URL"]+'/bolsones',
        headers=headers,
        data=json.dumps(data))
    bolsones = json.loads(r.text)["bolsones"]
    if r.status_code == 404:
        return redirect(url_for('inicio.html'))
    return render_template('bolsones_no_logueado.html', bolsones=bolsones)
