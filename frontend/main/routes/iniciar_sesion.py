from flask import Blueprint, render_template, redirect, url_for, current_app, request
from ..forms.iniciar_sesion_from import LoginForm
from flask_login import login_required, LoginManager, current_user

# Crear Blueprint
iniciar_sesion = Blueprint('inicio_sesion', __name__, url_prefix='/inicio_sesion')


@iniciar_sesion.route('/inicio/')
def inicio():
    return render_template('inicio.html')


@iniciar_sesion.route('/registrarse/')
def registrarse():
    return render_template('registrarse.html')


@iniciar_sesion.route('/cambiar_contraseña/')
def cambiar_password():
    return render_template('cambiar_contraseña.html')
