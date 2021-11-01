import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, LoginManager, current_user
from ..forms.agregar_bolson_form import BolsonForms
from .auth import admin_required, proveedor_required

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/cuenta')
@login_required
def panel_admin():
    return render_template('panel_admin.html')


@admin.route('/consultar-compras')
def consultar_compras():
    return render_template('compras_admin.html')


@admin.route('/lista-proveedores')
def lista_proveedores():
    return render_template('lista_proveedores.html')


@admin.route('/agregar-bolson', methods=['POST', 'GET'])
@login_required
def agregar_bolson():
    return render_template('agregar_bolson.html')


@admin.route('/agregar-proveedor')
def agregar_proveedor():
    return render_template('agregar_proveedor.html')


@admin.route('/editar-perfil')
def editar_perfil():
    return render_template('editar_perfil.html')


@admin.route('/ver-productos')
def ver_productos():
    return render_template('ver_productos.html')


@admin.route('/ver-bolsones')
def ver_bolsones():
    return render_template('bolsones_admin.html')


@admin.route('/bolsones-pendientes')
@login_required
@admin_required
@proveedor_required
def bolsones_pendientes():
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Beares"+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsonespendientes',
        headers=headers)
    bolsones_pendientes = json.loads(r.text)["bolsonespendientes"]
    return render_template('bolsones_pendientes.html', bolsones_pendientes=bolsones_pendientes, user=user)


@admin.route('/bolsones-previos')
@login_required
@admin_required
@proveedor_required
def bolsones_previos():
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Beares"+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsonesprevios',
        headers=headers)
    bolsones_previos = json.loads(r.text)["Bolsones previos"]
    return render_template('bolsones_previos.html', bolsones_previos=bolsones_previos, user=user)
