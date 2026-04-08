class usuario:

    def __init__(self, USU_ID, USU_NOMBRE, USU_ROL, USU_CORREO, USU_CONTRASENA, USU_FAC_ID_FK):
        self.usu_id = USU_ID
        self.usu_nombre = USU_NOMBRE
        self.usu_rol = USU_ROL
        self.usu_correo = USU_CORREO
        self.usu_contrasena = USU_CONTRASENA
        self.usu_fac_id_fk = USU_FAC_ID_FK

    def todic(self):
        return {
            "id": int(self.usu_id) if self.usu_id else None,
            "nombre": self.usu_nombre,
            "rol": self.usu_rol,
            "correo": self.usu_correo,
            "contrasena": self.usu_contrasena,
            "factura_id": self.usu_fac_id_fk
        }