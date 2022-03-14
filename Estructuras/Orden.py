class Orden:

    def __init__(self, cliente, pizza):
        self.cliente = cliente
        self.pizza = pizza

    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente

    def setPizza(self, pizza):
        self.pizza = pizza

    def getPizza(self):
        return self.pizza

    def __str__(self):
        return 'Orden:  ' + str(self.cliente.nombre) + " Pizza: " + str(self.pizza.ingrediente) + " Tiempo:" + str(self.pizza.tiempo)

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

