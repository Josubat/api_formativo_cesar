from flask import current_app
from models.proveedor_model import provedor

def listarProvedores():
    c = current_app.mysql.connection.cursor()
    
    sql = "SELECT prov_id, prov_nombre, prov_contacto, prov_direccion, prov_email, prov_pro_id_fk FROM t_proveedor"
    c.execute(sql)
    datos = c.fetchall()
    
    lista = []
    
    for p in datos:
        pro = provedor(
             prov_id= int(p[0]) if str(p[0]).isdigit() else None,
            prov_nombre    = p[1],
            prov_contacto  = p[2],
            prov_direccion  = p[3],
            prov_email = p[4],
            prov_pro_id_fk    = p[5]
        ).todic()
        print("VALOR ID:", p[0], "TIPO:", type(p[0]))
        lista.append(pro)
    
    return lista
def registrarCliente():
    return

def editarCliente():
    return

def eliminarCliente():
    return

def buscarCliente():
    return

