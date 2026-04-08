from flask import current_app
from models.usuario_model import usuario

def listarUsuarios():
    c = current_app.mysql.connection.cursor()
    
    sql = """SELECT usu_id, usu_nombre, usu_rol, usu_correo, 
             usu_contrasena, usu_fac_id_fk FROM t_usuario"""
    c.execute(sql)
    datos = c.fetchall()
    
    lista = []
    
    for u in datos:
        obj = usuario(
            USU_ID=u[0],
            USU_NOMBRE=u[1],
            USU_ROL=u[2],
            USU_CORREO=u[3],
            USU_CONTRASENA=u[4],
            USU_FAC_ID_FK=u[5]
        ).todic()
        
        lista.append(obj)
    
    return lista