class cliente:

    def __init__(self, CLI_ID, CLI_NOMBRE, CLI_APELLIDO, CLI_TELEFONO, CLI_DIRECCION, CLI_CORREO):
        self.Cli_id = CLI_ID
        self.Cli_nombre = CLI_NOMBRE
        self.Cli_apellido = CLI_APELLIDO
        self.Cli_telefono = CLI_TELEFONO
        self.Cli_direccion = CLI_DIRECCION
        self.Cli_correo = CLI_CORREO

    def todic(self):
        return {
            "id": int(self.Cli_id) if self.Cli_id is not None else None, 
            "nombre": self.Cli_nombre,
            "apellido": self.Cli_apellido,
            "telefono": self.Cli_telefono,  
            "direccion": self.Cli_direccion,
            "correo": self.Cli_correo
        }