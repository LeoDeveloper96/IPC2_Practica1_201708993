class Cliente:

    def __init__(self, nombre, nit, cel):
        self.nombre = nombre
        self.nit = nit
        self.cel = cel

    def __str__(self):
        return 'Cliente:  ' + str(self.nombre) + '\nnit: ' + str(self.nit) + '\ncel: ' + str(self.cel)