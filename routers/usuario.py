from flask import Blueprint
from controllers.usuario_controller import listar_usuarios_controller

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/')
def listar():
    return listar_usuarios_controller()