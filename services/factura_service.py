from flask import current_app
from models.factura_model import factura

def listarFactura():
    c = current_app.mysql.connection.cursor()
    
    sql = "SELECT Fac_id, Fac_fecha_emision, Fac_email_enviado, Fac_forma_pago, Fac_total, Fac_Usu_id_fk FROM factura"
    c.execute(sql)
    datos = c.fetchall()
    
    lista = []
    
    for p in datos:
        fac = factura(
            FAC_ID = p[0] if p[0] else None,
            FAC_FECHA_EMISION = p[1],
            FAC_EMAIL_ENVIADO = p[2],
            FAC_FORMA_PAGO = p[3],
            FAC_TOTAL = p[4],
            FAC_USU_ID_FK = p[5]
        ).todic()
        lista.append(fac)
    
    return lista

def registrarFactura():
    try:
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO factura (Fac_id, Fac_fecha_emision, Fac_email_enviado, 
                 Fac_forma_pago, Fac_total, Fac_Usu_id_fk) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        # Los datos vendrán del request en el controller
        return {"mensaje": "Factura registrada correctamente"}
    except Exception as e:
        return {"error": str(e)}

def editarFactura():
    try:
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE factura SET Fac_fecha_emision=%s, Fac_email_enviado=%s, 
                 Fac_forma_pago=%s, Fac_total=%s, Fac_Usu_id_fk=%s 
                 WHERE Fac_id=%s"""
        # Los datos vendrán del request en el controller
        return {"mensaje": "Factura actualizada correctamente"}
    except Exception as e:
        return {"error": str(e)}

def eliminarFactura():
    try:
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM factura WHERE Fac_id=%s"
        # El id vendrá del request en el controller
        return {"mensaje": "Factura eliminada correctamente"}
    except Exception as e:
        return {"error": str(e)}

def buscarFactura():
    try:
        c = current_app.mysql.connection.cursor()
        # Se puede buscar por varios criterios
        sql = "SELECT Fac_id, Fac_fecha_emision, Fac_email_enviado, Fac_forma_pago, Fac_total, Fac_Usu_id_fk FROM factura WHERE Fac_id=%s"
        # El criterio de búsqueda vendrá del request en el controller
        c.execute(sql)
        datos = c.fetchall()
        
        lista = []
        for p in datos:
            fac = factura(
                FAC_ID = p[0] if p[0] else None,
                FAC_FECHA_EMISION = p[1],
                FAC_EMAIL_ENVIADO = p[2],
                FAC_FORMA_PAGO = p[3],
                FAC_TOTAL = p[4],
                FAC_USU_ID_FK = p[5]
            ).todic()
            lista.append(fac)
        
        return lista
    except Exception as e:
        return {"error": str(e)}
