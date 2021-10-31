from .. forms.agregar_bolson_form import BolsonForms
from .. forms.compras_form import CompraForms
import json
import requests
from flask_login import login_required, LoginManager, current_user
from flask import redirect, render_template, url_for, Blueprint, current_app, request
from .auth import admin_required, proveedor_required

bolsones = Blueprint('bolsones', __name__, url_prefix='/bolsones')


@bolsones.route('/bolsones_venta')
@login_required
def bolsones_registrado():
    r = requests.get(f'{current_app.config["API_URL"]}/bolsones-venta',
                     headers={"content-type": "application/json"},)
    bolsones = json.loads(r.text)["bolsonesventa"]
    return render_template('ver_bolsones_registrado.html', bolsones=bolsones)


@bolsones.route('/bolsones-venta')
def ver():
    user = current_user
    auth = request.cookies['access_token']
    print("1111111111111")
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer'+auth}
    print("222222222222222222")
    r = requests.get(
        print("444444444444444"),
        current_app.config["API_URL"]+'/bolsones',
        headers=headers
    )
    print("666666666")
    bolsones = json.loads(r.text)["bolsones"]
    return render_template('bolsones_no_logueado.html', bolsones=bolsones)


@bolsones.route('/bolsones-pendientes')
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
        headers=headers,
        data=json.dumps(data)
    )
    bolsones_pendientes = json.loads(r.text)["Bolsones pendientes"]
    return render_template('bolsones_pendientes.html', bolsones_pendientes=bolsones_pendientes, user=user)


@bolsones.route('/bolsones-previos')
@login_required
@admin_required
@proveedor_required
def bolsones_pendientes():
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Beares"+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsonesprevios',
        headers=headers,
        data=json.dumps(data)
    )
    bolsones_previos = json.loads(r.text)["Bolsones previos"]
    return render_template('bolsones_previos.html', bolsones_previos=bolsones_previos, user=user)
