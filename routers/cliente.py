from flask import blueprint
from controllers.cliente_controlles import cnlistado

clientes_bp = blueprint('clientes', __name__)
@clientes_bp.route('/')
def listado():
    return cnlistado()

