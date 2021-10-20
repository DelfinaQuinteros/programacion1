from typing import Any

import json
import requests

from flask import redirect, render_template, url_for, Blueprint, current_app

ver_bolsones = Blueprint('ver_bolsones', __name__, url_prefix='/ver_bolsones')


@ver_bolsones.route('/bolsones_venta/<int:page>')
def bolsones_registrado(page):
    page = {"page": int(page)}
    r = requests.get(f'{current_app.config["API_URL"]}/bolsones-venta', headers={"content-type": "application/json"},
                     json=page)

    bolsones = json.loads(r.text)["bolsonesventa"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]
    return render_template('ver_bolsones_registrado.html', bolsones=bolsones, page=page, pages=pages)


@ver_bolsones.route('/bolsones-sin-logear/<int:id>')
def ver(id):
    data = {}
    data[page] = 1
    headers = {'content-type': 'application/json'}
    r = requests.get(
        current_app.config["API_URL"]+'/bolsones',
        headers=headers,
        data=json.dumps(data)
    )
    bolsones = json.loads(r.text)["bolsones"]
    r = requests.get(
        current_app.config["API_URL"]+'/bolsonespendientes',
        headers=headers,
        data=json.dumps(data)
    )
    bolsones_pendientes = json.loads(r.text)["Bolsones pendientes"]
    return render_template('bolsones_no_logueado.html', bolsones=bolsones, bolsones_pendientes=bolsones_pendientes)


@ver_bolsones.route('/inicio_sesion/')
def inicio_sesion():
    """usar create y poner los datos de inicio de sesion con el form"""
    return render_template('inicio_sesion.html')


@ver_bolsones.route('/registrarse/')
def registrarse():
    """usar create y poner los datos de registrarse con el form"""
    return render_template('registrarse.html')