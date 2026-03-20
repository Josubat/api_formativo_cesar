from flask import current_app
from models.cliente_model import cliente

def listadoCliente():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM cliente"
    c.execute(sql)
    datos = c.fetchall()
    return datos

def registrarCliente():
    return

def editarCliente():
    return

def eliminarCliente():
    return

def buscarCliente():
    return

