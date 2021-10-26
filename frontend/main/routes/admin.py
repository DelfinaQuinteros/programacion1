import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, LoginManager, current_user
from ..forms.iniciar_sesion_form import LoginForm
from ..forms.registrarse_form import RegistrarseForm
from .auth import admin_required, proveedor_required

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/panel-admin')
def panel_admin():
    return render_template('panel_admin.html')


@admin.route('/lista-proveedores')
def lista_proveedores():
    return render_template('lista_proveedores.html')


@admin.route('/agregar-bolson')
def agregar_bolson():
    return render_template('agregar_bolson.html')


@admin.route('/agregar-proveedor')
def agregar_proveedor():
    return render_template('agregar_proveedor.html')


@admin.route('/editar-perfil')
def editar_perfil():
    return render_template('editar_perfil.html')


@admin.route('/ver-bolsones')
def ver_bolsones():
    return render_template('bolsones_admin.html')
