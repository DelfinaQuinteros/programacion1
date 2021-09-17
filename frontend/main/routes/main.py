from flask import Blueprint, redirect, url_for
from . import inicio

#Crear Blueprint
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    #Redireccionar a función de vista
    return redirect(url_for('inicio.index'))
