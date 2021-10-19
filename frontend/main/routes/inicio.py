import json
import requests
from flask import Blueprint, current_app, render_template

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
    return render_template('bolsones_no_logeado.html')
