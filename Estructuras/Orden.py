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
