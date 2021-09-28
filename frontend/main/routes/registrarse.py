from flask import Blueprint, render_template

# Crear Blueprint
registrarse = Blueprint('registrarse', __name__, url_prefix='/registrarse')


@registrarse.route('/')
def index():
    return render_template('registrarse.html')


@registrarse.route('/inicio/<int:id>')
def inicio(id):
    return render_template('inicio.html')


@registrarse.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')




