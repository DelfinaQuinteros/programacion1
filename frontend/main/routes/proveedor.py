import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, LoginManager, current_user
from ..forms.modificar_datos_form import ModificarDatosForm
from ..forms.registrarse_form import RegistrarseForm
from .auth import admin_required, proveedor_required

proveedor = Blueprint('proveedor', __name__, url_prefix='/proveedor')


@proveedor.route('/regitrar', methods=['POST', 'GET'])
def registrar():
    form = RegistrarseForm
    if form.validate_on_submit():
        print(form.nombre.data)
        return redirect(url_for('main.index'))
    return render_template('agregar_proveedor.html', form=form)


@proveedor.route('/ver_productos')
def ver_productos():
    return render_template('ver_productos')


# modificar, eliminar y agregar productos
@proveedor.route('/modificar-producto')
def modificar_producto():
    return render_template('modificar_producto_prov.html')


@proveedor.route('/panel-proveedor')
def panel_proveedor():
    return render_template('panel_proveedor.html')


@proveedor.route('/editar-perfil')
def editar_perfil():
    return render_template('editar_perfil.html')
