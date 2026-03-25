class Factura:
    def __init__(self, fac_id, fac_fecha_emision, fac_email_enviado, fac_forma_pago, fac_total, fac_usu_id_fk):
        self.id-factura = fac_id
        self.fecha = fac_fecha_emision
        self.total = fac_email_enviado
        self.estado = fac_forma_pago
        self.id-usuario = fac_total
        self.id-usuario = fac_usu_id_fk

def todic(self):
        return {
            "id": int(self.fac_id) if self.fac_id is not None else None, 
            "fecha": self.fac_fecha_emision,
            "total": float(self.fac_total) if self.fac_total is not None else None,
            "estado": self.fac_forma_pago,
            "id-usuario": int(self.fac_usu_id_fk) if self.fac_usu_id_fk is not None else None
        }
