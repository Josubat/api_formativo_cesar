from flask import Blueprint
from controllers.proveedor_producto_controller import listar_proveedor_productos_controller

proveedor_productos_bp = Blueprint('proveedor_productos', __name__)

@proveedor_productos_bp.route('/')
def listar():
    return listar_proveedor_productos_controller()