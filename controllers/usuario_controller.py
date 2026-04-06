from flask import jsonify
from services.usuario_service import listarUsuarios

def listar_usuarios_controller():
    try:
        datos = listarUsuarios()
        return jsonify(datos), 200

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500