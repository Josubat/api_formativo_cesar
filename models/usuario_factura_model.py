class usuario_factura:

    def __init__(self, USA_USU_ID_FK, USA_FAC_ID_FK):
        self.usa_usu_id_fk = USA_USU_ID_FK
        self.usa_fac_id_fk = USA_FAC_ID_FK

    def todic(self):
        return {
            "usuario_id": int(self.usa_usu_id_fk) if self.usa_usu_id_fk else None,
            "factura_id": int(self.usa_fac_id_fk) if self.usa_fac_id_fk else None
        }