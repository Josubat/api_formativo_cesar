class factura:
    def __init__(self, FAC_ID=None, FAC_FECHA_EMISION=None, FAC_EMAIL_ENVIADO=None, 
                 FAC_FORMA_PAGO=None, FAC_TOTAL=None, FAC_USU_ID_FK=None):
        self.FAC_ID = FAC_ID
        self.FAC_FECHA_EMISION = FAC_FECHA_EMISION
        self.FAC_EMAIL_ENVIADO = FAC_EMAIL_ENVIADO
        self.FAC_FORMA_PAGO = FAC_FORMA_PAGO
        self.FAC_TOTAL = FAC_TOTAL
        self.FAC_USU_ID_FK = FAC_USU_ID_FK
    
    def todic(self):
        return {
            "FAC_ID": self.FAC_ID,
            "FAC_FECHA_EMISION": self.FAC_FECHA_EMISION,
            "FAC_EMAIL_ENVIADO": self.FAC_EMAIL_ENVIADO,
            "FAC_FORMA_PAGO": self.FAC_FORMA_PAGO,
            "FAC_TOTAL": self.FAC_TOTAL,
            "FAC_USU_ID_FK": self.FAC_USU_ID_FK
        }
