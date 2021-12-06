import json
import requests
from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, LoginManager, current_user
from ..forms.agregar_bolson_form import BolsonForms
from .auth import admin_required, proveedor_required
from ..forms.modificar_datos_form import ModificarDatosForm
from ..forms.agregar_proveedor_form import AgregarProveedorForm
from ..forms.agregar_bolson_form import BolsonForms, FormFilterBolsones, FormFilterBolson
from ..forms.registrarse_form import RegistrarseForm
from ..forms.producto_form import FormFilterProducto

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/cuenta')
@login_required
@admin_required
def panel_admin():
    return render_template('panel_admin.html')


@admin.route('/consultar-compras')
@login_required
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
@login_required
def lista_proveedores():
    return render_template('lista_proveedores.html')


@admin.route('/agregar-bolson', methods=['POST', 'GET'])
@login_required
@admin_required
def agregar_bolson():
    form = BolsonForms()
    auth = request.cookies['access_token']
    headers = {'content-type': "application/json",
               'authorization': "Bearer " + auth}
    data = {'page': 1}
    r = requests.get(current_app.config["API_URL"]+'/productos',
                    headers=headers,
                    data=json.dumps(data))
    productos = [(producto['id'], producto['nombre']) for producto in json.loads(r.text)["productos"]]
    productos.insert(0, (0, '--Seleccionar producto'))
    form.producto.choices = productos
    form.producto2.choices = productos
    form.producto3.choices = productos
    form.producto4.choices = productos
    form.producto5.choices = productos

    if form.validate_on_submit():
        data = {}
        data["nombre"] = form.nombre.data
        data["fecha"] = form.fecha.data
        data["precio"] = form.precio.data
        data["productos"] = form.productosId.data
        data["aprobado"] = form.aprobado.data
        print(data)
        r = requests.post(current_app.config["API_URL"]+'/bolsonespendientes',
                          headers=headers,
                          data=json.dumps(data))
        if r.status_code == 200:
            flash("Bolson creado con exito", "success")
            return redirect(url_for('admin.panel_admin'))
    return render_template('agregar_bolson.html', form=form)


@admin.route('/agregar-proveedor', methods=['POST', 'GET'])
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


@admin.route('/eliminar-proveedor/<int:id>')
@login_required
@admin_required
def eliminar_proveedor(id):
    auth = request.cookies['access_token']
    headers = {'content-type': "application/json",
               'authorization': "Bearer " + auth}
    r = requests.delete(current_app.config['API_URL'] + '/proveedor/' + str(id),
                        headers=headers)
    if r.status_code == 404:
        flash('El proveedor no existe', 'danger')
        return redirect('admin.lista_proveedores')
    flash('El proveedor ha sido eliminado', 'success')
    return redirect('admin.lista_proveedores')


@admin.route('/editar-perfil/<int:id>', methods=['POST', 'GET'])
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


@admin.route('/bolsones')
@login_required
@admin_required
def ver_todos():
    user = current_user
    filter = FormFilterBolsones(request.args, meta={'csrf': False})
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Bearer"+auth}
    data = {}
    data['page'] = 1
    data['per_page'] = 5
    if 'page' in request.args:
        data['page'] = request.args.get('page', '')
    if filter.submit():
        if filter.desde.data is not None:
            data['desde'] = filter.desde.data.strftime('%Y-%m-%d')
        if filter.hasta.data is not None:
            data['hasta'] = filter.hasta.data.strftime('%Y-%m-%d')
    r = requests.get(current_app.config['API_URL']+'/bolsones',
                     headers=headers,
                     data=json.dumps(data))
    bolsones = json.loads(r.text)["bolsones"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('ver_todos.html', pagination=pagination, bolsones=bolsones, filter=filter, user=user)


@admin.route('/ver-productos')
def ver_productos():
    filter = FormFilterProducto(request.args, meta={'csrf': False})
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Bearer" + auth}
    data = {}
    data['page'] = 1
    data['per_page'] = 5
    if 'page' in request.args:
        data['page'] = request.args.get('page', '')
    data_prov = {}
    data_prov['page'] = 1
    r = requests.get(
        current_app.config['API_URL']+'/proveedores',
        headers=headers,
        data=json.dumps(data_prov))
    proveedores = [(item['id'], item['nombre']+""+item["apellido"]) for item in json.loads(r.text)["proveedores"]]
    proveedores.insert(0, (0, "Proveedor"))
    filter.proveedorid.choices = proveedores
    if filter.submit():
        if filter.productos.data is not None and filter.proveedorid != 0:
            data['proveedorid'] = filter.proveedorid.data
        if filter.ordenamiento.data != 0:
            data['ordenamiento'] = filter.ordenamiento.data
    r = requests.get(
        f'{current_app.config["API_URL"]}/productos',
        headers={'content-type': "application/json",
                 'authorization': "Bearer " + auth},
        json=data
    )
    productos = json.loads(r.text)['productos']
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('ver_productos.html', productos=productos, pagination=pagination, filter=filter)


@admin.route('/producto-eliminar/<int:id>')
def eliminar_producto(id):
    auth = request.cookies['access_token']
    r = requests.delete(f'{current_app.config["API_URL"]}/producto/{id}',
                        headers={'content-type': "application/json",
                                 'authorization': "Bearer " + auth})
    return redirect(url_for('admin.ver_productos'))


@admin.route('/ver-compras')
@admin_required
def ver_compras():
    data = {'per_page': 3}
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer' + auth}
    r = requests.get(
        current_app.config["API_URL"] + '/compras',
        headers=headers,
        json=data
    )
    bolsones = json.loads(r.text)["compras"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('compras_admin.html', bolsones=bolsones, user=user, pagination=pagination)


@admin.route('/bolsones-pendientes')
def bolsones_pendientes():
    filter = FormFilterBolsones(request.args, meta={'csrf': False})
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Beares" + auth}
    data = {}
    data['page'] = 1
    data['per_page'] = 5
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    if filter.submit():
        if filter.desde.data is not None:
            data['desde'] = filter.desde.data.strftime('%Y-%m-%d')
        if filter.hasta.data is not None:
            data['hasta'] = filter.hasta.data.strftime('%Y-%m-%d')
    r = requests.get(
        current_app.config["API_URL"] + '/bolsonespendientes',
        headers=headers,
        json=data)
    bolsones = json.loads(r.text)["bolsonespendientes"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('bolsones_pendientes.html', bolsones=bolsones, user=user, pagination=pagination, filter=filter)


@admin.route('/bolsones-previos')
def bolsones_previos():
    filter = FormFilterBolsones(request.args, meta={'csrf': False})
    data = {}
    data['page'] = 1
    data['per_page'] = 5
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    if filter.submit():
        if filter.desde.data is not None:
            data['desde'] = filter.desde.data.strftime('%Y-%m-%d')
        if filter.hasta.data is not None:
            data['hasta'] = filter.hasta.data.strftime('%Y-%m-%d')
    user = current_user
    auth = request.cookies['access_token']
    headers = {'content-type': 'application/json',
               'authorization': "Beares" + auth}
    r = requests.get(
        current_app.config["API_URL"] + '/bolsonesprevios',
        headers=headers,
        json=data)
    bolsones = json.loads(r.text)["bolsonesprevios"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('bolsones_previos.html', bolsones=bolsones, user=user, pagination=pagination, filter=filter)


@admin.route('/eliminar/<int:id>')
def eliminar(id):
    auth = request.cookies['access_token']
    headers = {
        'content-Type': "application/json",
        'authorization': "Bearer " + auth}
    r = requests.delete(
        current_app.config["API_URL"] + '/bolsonpendiente/' + str(id),
        headers=headers)
    if r.status_code == 204:
        return redirect(url_for('admin.ver_bolsones'))
