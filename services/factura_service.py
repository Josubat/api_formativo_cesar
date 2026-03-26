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
