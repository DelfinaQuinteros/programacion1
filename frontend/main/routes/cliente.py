import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request, make_response
from flask_login import login_required, LoginManager, current_user
from ..forms.iniciar_sesion_form import LoginForm
from ..forms.registrarse_form import RegistrarseForm
from ..forms.modificar_datos_form import ModificarDatosForm

cliente = Blueprint('cliente', __name__, url_prefix='/cliente')


@cliente.route('/bolsones')
@login_required
def bolsones_en_venta():
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer'+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsones',
        headers=headers,
        json={}
    )
    bolsones = json.loads(r.text)["bolsones"]
    return render_template('ver_bolsones_registrado.html', bolsones=bolsones)


@cliente.route('/bolsones-no-logeado/')
def bolsones_no_logeado():
    headers = {'content-type': 'application/json'}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsones',
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
               "authorization": "Bearer"+auth}
    r = requests.get(
        current_app.config["API_URL"]+'/cliente',
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
        return redirect(url_for('inicio_sesion.html'))
    return render_template('registrarse.html', form=form)


@cliente.route('/editar-perfil')
def editar_perfil(id: int):
    form = PerfilForm()
    if not form.is_submitted():
        r = requests.get(
            f'{current_app.config["API_URL"]}/usuario/{int(id)}',
            headers={"content-type": "application/json"},
            auth=BearerAuth(str(request.cookies['access_token']))
        )
    try:
        usuario = json.loads(r.text)
        form.nombre.data = usuario['nombre']
        form.apellido.data = usuario['apellido']
        form.telefono.data = usuario['telefono']
        form.email.data = usuario['email']
    except:
        pass

    return form



@cliente.route('/ver-compras')
def ver_compras():
    return not render_template('compra_cliente.html')



