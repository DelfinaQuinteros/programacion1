from flask import Blueprint, render_template

# Crear Blueprint
inicio = Blueprint('inicio', __name__, url_prefix='/inicio')


@inicio.route('/')
def index():
    # Mostrar template
    return render_template('inicio.html')


@inicio.route('/view/<int:id>')
def view(id):
    # Mostrar template
    return render_template('inicio_registrado.html')
