from flask import jsonify
from services.proveedor_producto_service import listarProveedorProductos

def listar_proveedor_productos_controller():
    try:
        datos = listarProveedorProductos()
        return jsonify(datos), 200

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500