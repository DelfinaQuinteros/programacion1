import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, LoginManager, current_user
from ..forms.iniciar_sesion_form import LoginForm
from ..forms.registrarse_form import RegistrarseForm

cliente = Blueprint('cliente', __name__, url_prefix='/cliente')


@cliente.route('/bolsones')
def bolsones_en_venta():
    return render_template('inicio_registrado.html')


@cliente.route('/bolsones-no-logeado')
def bolsones_no_logueaedo():
    data = {'page': 1}
    headers = {'content-type': 'application/json'}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsones',
        headers=headers,
        data=json.dumps(data))
    bolsones = json.loads(r.text)["bolsones"]
    if r.status_code == 200:
        r = r.json()
    elif r.status_code == 404:
        return redirect(url_for('inicio.html'))
    elif r.status_code == 500:
        return redirect(url_for('inicio.html'))
    return render_template('bolsones_no_logueado.html', bolsones=bolsones)


@cliente.route('/cuenta/<int:id>')
@login_required
def cuenta():
    auth = request.cookies['access_token']
    headers = {"content-type": "application/json",
               "authorization": "Bearer"+auth}
    r = request.get(
        current_app.config["API_URL"]+'/cliente/'+str(id),
        headers=headers)
    if r.status_code == 404:
        return redirect(url_for('inicio_registrado.html'))
    cliente = json.loads(r.text)
    return render_template('panel_cliente.html', cliente=cliente)


@cliente.route('/iniciar-sesion', methods=['POST', 'GET'])
def inicio_sesion():
    form = LoginForm()
    if form.validate_on_submit():
        data = {"email": form.email.data, "password": form.password.data}
        headers = {"content-type": "application/json"}
        r = request.post(
            current_app.config["API_URL"] + '/auth/login',
            headers=headers,
            data=json.dumps(data))
        return redirect(url_for('inicio.html'))
    return render_template('inicio_sesion.html', formulario=form)


@cliente.route('/registrarse', methods=['POST', 'GET'])
def registrarse():
    form = RegistrarseForm()
    if form.validate_on_submit():
        data = {"nombre": form.nombre.data, "apellido": form.apellido.data, "E-mail": form.email.data,
                "password": form.password.data, "Confirm": form.password.data}
        print(data)
        headers = {
            'content-type': "application/json"
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/register',
            headers=headers,
            data=json.dumps(data))
        return redirect(url_for('inicio.html'))
    return render_template('registrarse.html', form=form)
