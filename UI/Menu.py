from pip._vendor.distlib.compat import raw_input
import re

from Estructuras.Cliente import Cliente
from Estructuras.Cola import Cola
from Estructuras.Orden import Orden
from Estructuras.Pizza import Pizza


class Menu:

    cola = Cola()

    def menu(self):
        print("\n")
        print("1 Agregar orden")
        print("2 Mostrar elementos de la cola")
        print("3.Desencolar")
        print("4 Graficar Cola")
        print("5 Salir")
        entrada = input("Ingrese un numero 1-5" + "\n")
        patron = "[1-3]{1}"

        # cláusula de guarda
        if not re.search(patron, entrada): return self.menu()
        if entrada == "1":
            self.submenu1()
            self.menu()
        elif entrada == "2":
            self.cola.mostrarCola(self.cola)
            self.menu()
        elif entrada == "3":
            self.cola.desencolar()
            self.menu()
        elif entrada == "4":
            pass
        elif entrada == "5":
            raw_input("Presione una tecla" + "\n")

    def submenu1(self):
        print("------------------------------------------")
        # Cliente
        nombre = input("Ingrese el nombre del cliente" + "\n")
        nit = input("Ingrese el numero de nit" + "\n")
        telefono = input("Ingrese el telefono del cliente" + "\n")

        print("------------------------------------------")
        # Pizza
        ingrediente = input("Ingrese el ingrediente de la pizza" + "\n")
        cantidad = input("Ingrese la cantidad" + "\n")
        self.cola.encolar(Orden(Cliente(nombre,nit,telefono),Pizza(ingrediente,cantidad)))