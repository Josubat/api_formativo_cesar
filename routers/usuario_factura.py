from flask import Blueprint
from controllers.usuario_factura_controller import listar_usuario_factura_controller

usuario_factura_bp = Blueprint('usuario_factura', __name__)

@usuario_factura_bp.route('/')
def listar():
    return listar_usuario_factura_controller()