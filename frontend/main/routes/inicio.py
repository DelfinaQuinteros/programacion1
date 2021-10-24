import json
import requests
from flask import Blueprint, current_app, render_template, redirect, url_for, request

# Crear Blueprint
inicio = Blueprint('inicio', __name__, url_prefix='/inicio')


@inicio.route('/')
def index():
    # Mostrar template
    return render_template('inicio.html')


@inicio.route('/inicio-registrado')
def inicio_logeado():
    return render_template('inicio_registrado.html')


@inicio.route('/inicio-no-registrado')
def inicio_no_logeado():
    return render_template('inicio.html')
