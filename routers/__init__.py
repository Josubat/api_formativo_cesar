from .cliente import clientes_bp
from .pedido import pedido_bp

def cargarruta(app):
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(pedido_bp, url_prefix='/pedidos')