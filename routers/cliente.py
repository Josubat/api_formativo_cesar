from flask import Blueprint
<<<<<<< HEAD
from controllers.cliente_controllers import cnlistado
=======
from controllers.cliente_controllers import cnlistado, cnregistrarcliente
>>>>>>> 01532b250e8ff3fde7bbe648d1a5577e6f6dc951

clientes_bp = Blueprint('clientes', __name__)
@clientes_bp.route('/')
def listado():
    return cnlistado()

@clientes_bp.route('/',methods=["post"]) 
def registrar():
    return cnregistrarcliente()