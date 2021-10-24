import json
import requests
from flask import Blueprint, redirect, url_for, current_app, make_response, flash
from flask_login import login_user, logout_user

from .auth import User
from ..forms.iniciar_sesion_form import LoginForm

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    return redirect(url_for('inicio.index'))


@main.route('/login', methods=['POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        data = '{"email":"' + loginForm.email.data + '", "password":"' + loginForm.password.data + '"}'
        r = requests.post(
            current_app.config["API_URL"] + '/auth/login',
            headers={"content-type": "application/json"},
            data=data)
        if r.status_code == 200:
            user_data = json.loads(r.text)
            user = User(id=user_data.get("id"), email=user_data.get("email"), role=user_data.get("role"))
            login_user(user)
            req = make_response(redirect(url_for('inicio.index')))
            req.set_cookie('access_token', user_data.get("access_token"), httponly=True)
            return req
        else:
            flash('Usuario o contraseña incorrecta', 'danger')
    return redirect(url_for('inicio.html'))


@main.route('/logout')
def logout():
    req = make_response(redirect(url_for('inicio.index')))
    req.set_cookie('access_token', '', httponly=True)
    req.delete_cookie('access_token', httponly=False)
    logout_user()
    return req
