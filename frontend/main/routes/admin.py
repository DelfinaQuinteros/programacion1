import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, LoginManager, current_user
from ..forms.agregar_bolson_form import BolsonForms
from .auth import admin_required, proveedor_required
from ..forms.modificar_datos_form import ModificarDatosForm
from ..forms.agregar_proveedor_form import AgregarProveedorForm
from ..forms.registrarse_form import RegistrarseForm

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/cuenta')
@login_required
def panel_admin():
    return render_template('panel_admin.html')


@admin.route('/consultar-compras')
def consultar_compras():
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer' + auth}
    r = requests.get(
        current_app.config["API_URL"] + '/bolsonesventa',
        headers=headers,
        json={}
    )
    bolsones = json.loads(r.text)["bolsonesventa"]
    return render_template('compras_admin.html', bolsones=bolsones, user=user)


@admin.route('/lista-proveedores')
def lista_proveedores():
    return render_template('lista_proveedores.html')


@admin.route('/agregar-bolson', methods=['POST', 'GET'])
@login_required
def agregar_bolson():
    return render_template('agregar_bolson.html')


@admin.route('/agregar-proveedor', methods=['POST', 'GET'])
@admin_required
@login_required
def agregar_proveedor():
    form = AgregarProveedorForm()
    if form.validate_on_submit():
        data = {"nombre": form.nombre.data, "apellido": form.apellido.data, "email": form.email.data,
                "password": form.password.data, "role": "proveedor"}
        headers = {
            'content-type': "application/json"
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/register',
            headers=headers,
            data=json.dumps(data))
    return render_template('agregar_proveedor.html', form=form)


@admin.route('/editar-perfil/<int:id>', methods=['POST', 'GET'])
def editar_perfil(id):
    auth = request.cookies['access_token']
    form = ModificarDatosForm()
    usuario = {
        "nombre": form.nombre.data,
        "apellido": form.apellido.data,
        "telefono": form.telefono.data,
        "password": form.password.data
    }

    r = requests.put(current_app.config['API_URL'] + '/cliente/' + str(id),
                     headers={'content-type': "application/json",
                              'authorization': "Bearer " + auth},
                     json=usuario
                     )
    return render_template('editar_perfil.html', form=form, id=id)


@admin.route('/ver-productos')
def ver_productos():
    return render_template('ver_productos.html')


@admin.route('/ver-bolsones')
@admin_required
def ver_bolsones():
    data = {'per_page': 3}
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer' + auth}
    r = requests.get(
        current_app.config["API_URL"] + '/bolsonesventa',
        headers=headers,
        json=data
    )
    bolsones = json.loads(r.text)["bolsonesventa"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('bolsones_admin.html', bolsones=bolsones, user=user, pagination=pagination)


@admin.route('/bolsones-pendientes')
def bolsones_pendientes():
    data = {'per_page': 3}
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Beares"+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsonespendientes',
        headers=headers,
        json=data)
    bolsones = json.loads(r.text)["bolsonespendientes"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('bolsones_pendientes.html', bolsones=bolsones, user=user, pagination=pagination)


@admin.route('/bolsones-previos')
def bolsones_previos():
    data = {'per_page': 3}
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Beares"+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsonesprevios',
        headers=headers,
        json=data)
    bolsones = json.loads(r.text)["bolsonesprevios"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('bolsones_previos.html', bolsones=bolsones, user=user, pagination=pagination)
