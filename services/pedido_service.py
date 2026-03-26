from flask import current_app
from models.pedido_model import pedido

def listarPedido():
    c = current_app.mysql.connection.cursor()
    
    sql = "SELECT Ped_id, Ped_fecha, Ped_metodo_pago, Ped_estado_entrega, Ped_total, Ped_cli_id_fk, Ped_det_id_fk From pedido"
    c.execute(sql)
    reg = c.fetchall()
    
    listav = []
    
    for p in reg:
        ped = pedido(
            ID = int(p[0]) if str(p[0]).isdigit() else None,
            FECHA             = p[1],
            METODO_DE_PAGO    = p[2],
            ESTADO            = p[3],
            TOTAL             = p[4],
            ID_CLIENTE        = p[5],
            DETALLES          = p[6]
        ).a_diccionario()
        listav.append(ped)
        
    return listav