from flask import Blueprint, redirect, url_for
from . import bolsones

#Crear Blueprint
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    #Redireccionar a función de vista
    return redirect(url_for('bolsones.index'))
