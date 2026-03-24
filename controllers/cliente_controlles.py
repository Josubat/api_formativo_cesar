from flask import jsonify, request
from services.cliente_service import listarCliente

def cnlistado():
    datos = listarCliente()
    print(datos)