from .cliente import clientes_bp
from .pedido import pedido_bp
from .factura import facturas_bp

def cargarruta(app):
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(pedido_bp, url_prefix='/pedidos')
    app.register_blueprint(facturas_bp, url_prefix='/facturas')