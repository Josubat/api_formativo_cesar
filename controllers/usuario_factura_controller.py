from flask import jsonify
from services.usuario_factura_service import listarUsuarioFactura

def listar_usuario_factura_controller():
    try:
        datos = listarUsuarioFactura()
        return jsonify(datos), 200

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500