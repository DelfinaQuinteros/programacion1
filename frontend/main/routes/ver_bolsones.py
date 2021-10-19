from typing import Any

import json
import requests

from flask import redirect, render_template, url_for, Blueprint, current_app

ver_bolsones = Blueprint('ver_bolsones', __name__, url_prefix='/ver_bolsones')


@ver_bolsones.route('/bolsones_venta/<int:page>')
def venta(page):
    page = {"page": int(page)}
    r = requests.get(f'{current_app.config["API_URL"]}/bolsones-venta', headers={"content-type": "application/json"},
                     json=page)

    bolsones = json.loads(r.text)["bolsonesventa"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]
    return render_template('ver_bolsones_registrado.html', bolsones=bolsones, page=page, pages=pages)


@ver_bolsones.route('/bolsones/<int:id>')
def ver(id):
    r = requests.get(f'{current_app.config["API_URL"]}/bolson-venta/{id}',
                     headers={"content-type": "applications/json"}, json={})
    bolson = json.loads(r.text)
    bolsonId = bolson["id"]
    nombre = bolson["nombre"]
    fecha = bolson["fecha"]
    descripcion = bolson["descripcion"]

    json_api = {"bolsonId": int(id)}
    r = requests.get(f'{current_app.config["API_URL"]}/productos-bolsones',
                     headers={"content-type": "application/json"}, json=json_api)
    productos = json.loads(r.text)["productosbolsones"]
    return render_template('bolsones_no_logeado.html', title=f'{nombre}', bg_color="bg-secondary",
                           nombre=nombre, descripcion=descripcion, productos=productos
                           )


@ver_bolsones.route('/inicio_sesion/')
def inicio_sesion():
    """usar create y poner los datos de inicio de sesion con el form"""
    return render_template('inicio_sesion.html')


@ver_bolsones.route('/registrarse/')
def registrarse():
    """usar create y poner los datos de registrarse con el form"""
    return render_template('registrarse.html')
