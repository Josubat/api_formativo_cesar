from flask import Blueprint
from controllers.proveedor_controlles import cnlistado

proveedor_bp = Blueprint('provedor', __name__)
@proveedor_bp.route('/')
def listado():
    return cnlistado()