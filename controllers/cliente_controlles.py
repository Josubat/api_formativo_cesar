from flask import jsonify, request
from services.cliente_service import listarCliente

def cnlistado():
    try:
        datos = listarCliente()
        return jsonify(datos), 200

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500