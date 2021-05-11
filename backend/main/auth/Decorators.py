from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['role'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Solo administradores acceder', 403
    return wrapper


def admin_or_proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'proveedor' or claims['role'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Solo administradores o proveedores pueden acceder', 403
    return wrapper


def admin_or_cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'cliente' or claims['rol'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Solo administradores o clientes pueden acceder', 403
    return wrapper


@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return usuario.id


@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'role': usuario.role,
        'id': usuario.id,
        'mail': usuario.mail
    }
    return claims

