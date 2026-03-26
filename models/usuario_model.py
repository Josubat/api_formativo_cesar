class usuario:
    
    def __init__(self, Usu_id, Úsu_nombre, Usu_rol, Usu_correo, Usu_contraseña, Usu_Fac_id_fk):
        self.ID_Usuario = Usu_id
        self.Nombre_usuario = Úsu_nombre
        self.Rol_Usuario = Usu_rol
        self.Correo_Usuario = Usu_correo
        self.Contraseña_Usuario = Usu_contraseña
        self.ID_Factura_Usuario = Usu_Fac_id_fk