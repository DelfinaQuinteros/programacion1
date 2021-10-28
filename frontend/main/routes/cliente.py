import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request, make_response
from flask_login import login_required, LoginManager, current_user
from ..forms.iniciar_sesion_form import LoginForm
from ..forms.registrarse_form import RegistrarseForm

cliente = Blueprint('cliente', __name__, url_prefix='/cliente')


@cliente.route('/bolsones')
def bolsones_en_venta():
    return render_template('inicio_registrado.html')


@cliente.route('/bolsones-no-logeado/')
def bolsones_no_logueaedo():
    headers = {'content-type': 'application/json'}
    r = requests.get(
            current_app.config["API_URL"]+'/bolsones',
            headers=headers)
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
    return render_template('panel_cliente.html', cliente=cliente)


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
        data = {"nombre": form.nombre.data, "apellido": form.apellido.data, "E-mail": form.email.data,
                "contraseña": form.password.data, "Confirm": form.password.data}
        headers = {
            'content-type': "application/json"
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/register',
            headers=headers,
            data=json.dumps(data))
        return redirect(url_for('inicio.inicio_logeado'))
    return render_template('registrarse.html', form=form)


@cliente.route('/editar-perfil')
def editar_perfil():
    return render_template('editar_perfil.html')


@cliente.route('/ver-compras')
def ver_compras():
    return not render_template('compra_cliente.html')



