from flask import current_app
from models.proveedor_producto_model import proveedor_producto

def listarProveedorProductos():
    c = current_app.mysql.connection.cursor()
    
    sql = "SELECT ppp_prov_id_fk, ppp_pro_id_fk FROM t_proveedor_productos"
    c.execute(sql)
    datos = c.fetchall()
    
    lista = []
    
    for p in datos:
        obj = proveedor_producto(
            PPP_PROV_ID_FK=p[0],
            PPP_PRO_ID_FK=p[1]
        ).todic()
        
        lista.append(obj)
    
    return lista