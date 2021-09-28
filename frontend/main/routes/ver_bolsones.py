from flask import Blueprint, render_template

ver_bolsones = Blueprint('ver_bolsones', __name__, url_prefix='/ver_bolsones')


@ver_bolsones.route('/')
def index():
    return render_template('bolsones_no_logeado.html')


@ver_bolsones.route('/inicio_sesion/')
def inicio_sesion():
    return render_template('inicio_sesion.html')


@ver_bolsones.route('/registrarse/')
def registrarse():
    return render_template('registrarse.html')
