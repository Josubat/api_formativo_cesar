class proveedor_producto:

    def __init__(self, PPP_PROV_ID_FK, PPP_PRO_ID_FK):
        self.ppp_prov_id_fk = PPP_PROV_ID_FK
        self.ppp_pro_id_fk = PPP_PRO_ID_FK

    def todic(self):
        return {
            "proveedor_id": int(self.ppp_prov_id_fk) if self.ppp_prov_id_fk else None,
            "producto_id": int(self.ppp_pro_id_fk) if self.ppp_pro_id_fk else None
        }