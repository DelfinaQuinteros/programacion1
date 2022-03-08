import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request, flash
from flask_login import login_required, LoginManager, current_user
from ..forms.modificar_datos_form import ModificarDatosForm
from ..forms.registrarse_form import RegistrarseForm
from ..forms.producto_form import AgregarProductoForms
from .auth import admin_required, proveedor_required

proveedor = Blueprint('proveedor', __name__, url_prefix='/proveedor')


@proveedor.route('/registrar', methods=['POST', 'GET'])
def registrar():
    form = RegistrarseForm
    if form.validate_on_submit():
        print(form.nombre.data)
        return redirect(url_for('main.index'))
    return render_template('agregar_proveedor.html', form=form)


@proveedor.route('/agregar-producto', methods=['POST', 'GET'])
def agregar_producto():
    form = AgregarProductoForms()
    auth = request.cookies['access_token']
    if form.validate_on_submit():
        producto = {
            "nombre": form.nombre.data,
            "usuarioid": current_user.id
        }
        r = requests.post(current_app.config["API_URL"] + '/productos',
                          headers={'content-type': "application/json",
                                   'authorization': "Bearer " + auth},
                          json=producto)
        if r.status_code == 201:
            flash("Producto creado con exito", "success")
    return render_template('modificar_producto_prov.html', form=form)


@proveedor.route('/panel-proveedor')
def panel_proveedor():
    return render_template('panel_proveedor.html')


@proveedor.route('/editar-perfil/<int:id>', methods=['POST', 'GET'])
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
