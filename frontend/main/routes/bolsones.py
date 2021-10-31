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
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer'+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsones',
        headers=headers
    )
    bolsones = json.loads(r.text)["bolsones"]
    return render_template('bolsones_no_logueado.html', bolsones=bolsones)



