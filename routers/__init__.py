from .cliente import clientes_bp

def cargarruta(app):
    app.register_blueprint(clientes_bp, url_prefix='/clientes')