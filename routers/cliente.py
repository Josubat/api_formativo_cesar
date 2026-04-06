from flask import Blueprint
from controllers.cliente_controllers import cnlistado

clientes_bp = Blueprint('clientes', __name__)
@clientes_bp.route('/')
def listado():
    return cnlistado()

