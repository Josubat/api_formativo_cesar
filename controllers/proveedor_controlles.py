from flask import jsonify, request
from services.provedor_service import listarProveedores

def cnlistado():
    try:
        datos = listarProveedores()
        return jsonify(datos), 200

    except Exception as e:
        import traceback
        print(traceback.format_exc())  # 👈 ESTO ES LA CLAVE
        return jsonify({"error": str(e)}), 500