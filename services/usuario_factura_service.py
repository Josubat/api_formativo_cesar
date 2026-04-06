from flask import current_app
from models.usuario_factura_model import usuario_factura

def listarUsuarioFactura():
    c = current_app.mysql.connection.cursor()
    
    sql = "SELECT usa_usu_id_fk, usa_fac_id_fk FROM t_usuario_factura"
    c.execute(sql)
    datos = c.fetchall()
    
    lista = []
    
    for u in datos:
        obj = usuario_factura(
            USA_USU_ID_FK=u[0],
            USA_FAC_ID_FK=u[1]
        ).todic()
        
        lista.append(obj)
    
    return lista