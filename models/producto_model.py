class producto:
    def __init__(self, id=None, categoria=None, cantidad_disponible=None, precio=None, 
                 nombre=None, fecha_caducidad=None, descripcion=None, proveedor_id=None, detalle_id=None):
        self.id = id
        self.categoria = categoria
        self.cantidad_disponible = cantidad_disponible
        self.precio = precio
        self.nombre = nombre
        self.fecha_caducidad = fecha_caducidad
        self.descripcion = descripcion
        self.proveedor_id = proveedor_id
        self.detalle_id = detalle_id
    
    def todic(self):
        return {
            "id": self.id,
            "categoria": self.categoria,
            "cantidad_disponible": self.cantidad_disponible,
            "precio": self.precio,
            "nombre": self.nombre,
            "fecha_caducidad": self.fecha_caducidad,
            "descripcion": self.descripcion,
            "proveedor_id": self.proveedor_id,
            "detalle_id": self.detalle_id
        }