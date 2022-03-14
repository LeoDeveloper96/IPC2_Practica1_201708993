from pip._vendor.distlib.compat import raw_input
import re

from Estructuras.Cliente import Cliente
from Estructuras.Cola import Cola
from Estructuras.Orden import Orden
from Estructuras.Pizza import Pizza
import os
import webbrowser

class Menu:
    cola = Cola()

    def menu(self):
        print("\n")
        print("1 Agregar orden")
        print("2 Mostrar elementos de la cola")
        print("3 Desencolar")
        print("4 Graficar Cola")
        print("5 Tiempo total pizzas")
        print("6 Datos estudiante")
        print("7 Salir")
        entrada = input("Ingrese un numero 1-5" + "\n")
        patron = "[1-7]{1}"

        # cláusula de guarda
        if not re.search(patron, entrada): return self.menu()
        if entrada == "1":
            # self.submenu1()
            self.cola.encolar(Orden(Cliente("pablo", 123, 32145), Pizza("queso", 1)))
            self.cola.encolar(Orden(Cliente("pedro", 123, 32145), Pizza("queso", 1)))
            self.cola.encolar(Orden(Cliente("mario", 123, 32145), Pizza("queso", 1)))
            self.menu()
        elif entrada == "2":
            self.cola.mostrarCola(self.cola)
            self.menu()
        elif entrada == "3":
            self.cola.desencolar()
            self.menu()
        elif entrada == "4":
            self.graficar()
            self.menu()
            self.menu()
        elif entrada == "5":
            pass
            self.menu()
        elif entrada == "6":
            self.mostrarDatos()
            self.menu()
        elif entrada == "7":
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
        self.cola.encolar(Orden(Cliente(nombre, nit, telefono), Pizza(ingrediente, cantidad)))

    def graficar(self):
        contenido = ""
        contenido += "digraph cola" + "{" + "\n"
        contenido += "rankdir=LR;\n"
        contenido += "node [shape=record];\n"
        contador = 1
        for elemento in self.cola:
            contenido += str(contador) + "  [label=\"{ <data>" + elemento.datos + " | <ref>  }\"];\n"
            contador += 1
        for i in range(1, contador-1):
            contenido += str(i) + ": ref:c -> " + str(i+1) + ": data[arrowhead = vee, arrowtail = dot, dir = both, tailclip = false];\n"
        contenido += "\n" + "}"
        contenido += "\n"
        ruta = os.path.dirname(os.getcwd())
        file = open(ruta + "\\Graficas\\grafico.dot", "w+")
        file.write(contenido)
        file.close()
        os.system('cmd /C "dot -Tpng ' + ruta + '\\Graficas\\grafico.dot -o ' + ruta + '\\Graficas\\grafico.png"')
        webbrowser.open(ruta + '\\Graficas\\grafico.png')


    def mostrarDatos(self):
        print("Pablo Alejandro Franco Lemus")
        print("201708993")
        print("Introducción a la programacion y Computación 2")
        print("Ingenieria en Ciencias y Sistemas")
