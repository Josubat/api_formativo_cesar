class pedido:
    def __init__(self, ID, FECHA, METODO_DE_PAGO, ESTADO, TOTAL, ID_CLIENTE, DETALLES):
        self.Ped_id = ID
        self.Ped_fecha = FECHA
        self.Ped_metodo_pago = METODO_DE_PAGO
        self.Ped_estado_entrega = ESTADO
        self.Ped_total = TOTAL
        self.Ped_cli_id_fk = ID_CLIENTE
        self.Ped_det_id_fk = DETALLES

    def a_diccionario(self):
        return{
            "id": int(self.Ped_id) if self.Ped_id is not None else None,
            "fecha": str(self.Ped_fecha),
            "metodo_de_pag": self.Ped_metodo_pago,
            "estado": self.Ped_estado_entrega,
            "total": float(self.Ped_total),
            "cliente" : self.Ped_cli_id_fk,
            "detalles" : self.Ped_det_id_fk
        }