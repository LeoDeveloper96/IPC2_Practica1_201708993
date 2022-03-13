class Pizza:

    def __init__(self, ingrediente, cantidad):
        self.ingrediente = ingrediente
        self.tiempo = 0
        self.cantidad = cantidad

    def setTiempo(self):
        if self.ingrediente == "Pepperoni":
            self.tiempo = 3
        elif self.ingrediente == "Salchicha":
            self.tiempo = 4
        elif self.ingrediente == "Carne":
            self.tiempo = 10
        elif self.ingrediente == "Queso":
            self.tiempo = 5
        elif self.ingrediente == "Piña":
            self.tiempo = 2
        else:
            self.tiempo = 0

    def getTiempo(self):
        return self.tiempo

    def getIngrediente(self):
        return self.ingrediente

    def setIngrediente(self, ingrediente):
        self.ingrediente = ingrediente

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return 'Pizza:  ' + self.ingrediente + "\ntiempo: " + str(self.tiempo) + "\ncantidad: " + str(self.cantidad)