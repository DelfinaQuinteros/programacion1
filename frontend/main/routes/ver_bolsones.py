from flask import Blueprint, render_template
import requests, json
"""importar forms"""

ver_bolsones = Blueprint('ver_bolsones', __name__, url_prefix='/ver_bolsones')


@ver_bolsones.route('/')
def index():
    data = {}
    data['page'] = 1
    # Generar consulta GET al endpoint
    r = requests.get(
        current_app.config["API_URL"]+'/ver_bolsones',
        headers={"content-type":"application/json"},
        data = json.dumps(data))
    #Convertir respuesta de JSON a  diccionario
    print(r)
    bolsones_no_log = json.loads(r.text)["bolsones"]
    #Mostrar template
    return render_template('bolsones_no_logeado.html', bolsones_no_log=bolsones_no_log)


@ver_bolsones.route('/inicio_sesion/')
def inicio_sesion():
    """usar create y poner los datos de inicio de sesion con el form"""
    return render_template('inicio_sesion.html')


@ver_bolsones.route('/registrarse/')
def registrarse():
    """usar create y poner los datos de registrarse con el form"""
    return render_template('registrarse.html')
