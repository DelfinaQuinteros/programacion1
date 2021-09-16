from flask import Blueprint, render_template

# Crear Blueprint
professor = Blueprint('bolsones', __name__, url_prefix='/bolsones')


@professor.route('/')
def index():
    # Mostrar template
    return render_template('bolsones_list.html')


@professor.route('/view/<int:id>')
def view(id):
    # Mostrar template
    return render_template('bolsones_view.html')
