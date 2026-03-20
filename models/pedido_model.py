class pedido:
    def __init__(self, ID, FECHA, METODO_DE_PAGO, ESTADO, TOTAL, ID_CLIENTE, DETALLES):
        self.Ped_id = ID
        self.Ped_fecha = FECHA
        self.Ped_metodo_pago = METODO_DE_PAGO
        self.Ped_estado_entrega = ESTADO
        self.Ped_total = TOTAL
        self.Ped_cli_id_fk = ID_CLIENTE
        self.Ped_det_id_fk = DETALLES