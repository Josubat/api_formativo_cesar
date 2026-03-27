from flask import current_app
from models.cliente_model import cliente

def listarCliente():
    c = current_app.mysql.connection.cursor()
    
    sql = "SELECT cli_id, cli_nombre, cli_apellido, cli_telefono, cli_direccion, cli_correo FROM t_cliente"
    c.execute(sql)
    datos = c.fetchall()
    
    lista = []
    
    for p in datos:
        cli = cliente(
            CLI_ID = int(p[0]) if str(p[0]).isdigit() else None,
            CLI_NOMBRE    = p[1],
            CLI_APELLIDO  = p[2],
            CLI_TELEFONO  = p[3],
            CLI_DIRECCION = p[4],
            CLI_CORREO    = p[5]
        ).todic()
        print("VALOR ID:", p[0], "TIPO:", type(p[0]))
        lista.append(cli)
    
    return lista
def registrarCliente():
    return

def editarCliente():
    return

def eliminarCliente():
    return

def buscarCliente():
    return

