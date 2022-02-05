import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request, make_response, flash
from flask_login import login_required, LoginManager, current_user
from ..forms.iniciar_sesion_form import LoginForm
from ..forms.registrarse_form import RegistrarseForm
from ..forms.agregar_bolson_form import BolsonForms, FormFilterBolsones, FormFilterBolson
from ..forms.compras_form import FormFilterCompras
from ..forms.modificar_datos_form import ModificarDatosForm
from main.routes.auth import BearerAuth
from .auth import admin_required

cliente = Blueprint('cliente', __name__, url_prefix='/cliente')


@cliente.route('/bolsones')
@login_required
def bolsones_en_venta():
    filter = FormFilterBolson(request.args, meta={'csrf': False})
    data = {}
    data['page'] = 1
    data['per_page'] = 5
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer' + auth}
    if filter.submit():
        if filter.nombre.data is not None:
            data["nombre"] = filter.nombre.data
        if filter.desde.data is not None:
            data['desde'] = filter.desde.data.strftime('%Y-%m-%d')
        if filter.hasta.data is not None:
            data['hasta'] = filter.hasta.data.strftime('%Y-%m-%d')
        if filter.ordenamiento.data is not None:
            data['ordenamiento'] = filter.ordenamiento.data

    r = requests.get(
        current_app.config["API_URL"] + '/bolsonesventa',
        headers=headers,
        json=data
    )
    bolsones = json.loads(r.text)["bolsonesventa"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('ver_bolsones_registrado.html', bolsones=bolsones, user=user, pagination=pagination, filter=filter)


@cliente.route('/bolsones-no-logeado/')
def bolsones_no_logeado():
    headers = {'content-type': 'application/json'}
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones',
        headers=headers,
        json={}
    )
    bolsones = json.loads(r.text)["bolsones"]
    return render_template('bolsones_no_logeado.html', bolsones=bolsones)


@cliente.route('/cuenta')
@login_required
def panel_cliente():
    auth = request.cookies['access_token']
    headers = {"content-type": "application/json",
               "authorization": "Bearer" + auth}
    r = requests.get(
        current_app.config["API_URL"] + '/cliente',
        headers=headers)
    if current_user.role == 'cliente':
        return render_template('panel_cliente.html', cliente=cliente)
    elif current_user.role == 'admin':
        return render_template('panel_admin.html')
    elif current_user.role == 'proveedor':
        return render_template('panel_proveedor.html')


@cliente.route('/iniciar-sesion', methods=['POST', 'GET'])
def inicio_sesion():
    form = LoginForm()
    if form.validate_on_submit():
        data = {"email": form.email.data, "password": form.password.data}
        headers = {"content-type": "application/json"}
        r = requests.post(
            current_app.config["API_URL"] + '/auth/login',
            headers=headers,
            data=json.dumps(data))
        if r.status_code == 200:
            user_data = json.loads(r.text)
            req = make_response(redirect(url_for('inicio.inicio_logeado')))
            req.set_cookie('access_token', user_data.get("access_token"), httponly=True)
            return req
        else:
            flash('Usuario o contraseña incorrecta', 'danger')
    return render_template('inicio_sesion.html', form=form)


@cliente.route('/registrarse', methods=['POST', 'GET'])
def registrarse():
    form = RegistrarseForm()
    if form.validate_on_submit():
        data = {"nombre": form.nombre.data, "apellido": form.apellido.data, "email": form.email.data,
                "password": form.password.data}
        headers = {
            'content-type': "application/json"
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/register',
            headers=headers,
            data=json.dumps(data))
        return redirect(url_for('cliente.inicio_sesion'))
    return render_template('registrarse.html', form=form)


@cliente.route('/editar-perfil/<int:id>', methods=['POST', 'GET'])
@login_required
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


@cliente.route('/compras')
def ver_compras():
    data = {}
    data['page'] = 1
    data['per_page'] = 5
    if 'page' in request.args:
        data['page'] = request.args.get('page', '')
    auth = request.cookies['access_token']
    r = requests.get(current_app.config["API_URL"] + '/compras',
                     headers={"content-type": "applications/json",
                              'authorization': "Bearer " + auth},
                     data=data)
    compras = json.loads(r.text)["compras"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('compra_cliente.html', compras=compras, pagination=pagination)


@cliente.route('/comprar')
@login_required
def comprar():
    auth = request.cookies['access_token']
    headers = {"content-type": "applications/json",
               'authorization': "Bearer " + auth}
    data = {}
    data["bolsonid"] = id
    r = requests.post(
        current_app.config["API_URL"] + '/compras',
        headers=headers,
        data=json.dumps(data))
    if r.status_code == 200:
        flash('Compra realizada con exito', 'success')
        return redirect(url_for('cliente.panel_cliente'))
    return render_template('cliente.panel_cliente')


