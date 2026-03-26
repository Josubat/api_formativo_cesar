from flask import Blueprint
from controllers.pedido_controller import cnlistadoped

pedido_bp = Blueprint('pedidos', __name__)

@pedido_bp.route('/')
def listado_ped():
    return cnlistadoped()