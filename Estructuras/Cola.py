from Estructuras.Nodo import Nodo


class Cola:

    def __init__(self):
        self.cabeza = None

    # insertar al final
    def encolar(self, datos):
        if self.cabeza is None:
            self.cabeza = Nodo(datos, None)
            return
        iterador = self.cabeza
        while iterador.siguiente:
            iterador = iterador.siguiente
        iterador.siguiente = Nodo(datos, None)

    def eliminar_pos(self, indice):
        if indice < 0 or indice > self.get_length():
            raise Exception("Indice invalido")
        if indice == 0:
            self.cabeza = self.cabeza.siguiente
            return
        conteo = 0
        iterador = self.cabeza
        while iterador:
            if conteo == indice - 1:
                iterador.siguiente = iterador.siguiente.siguiente
                break
            iterador = iterador.siguiente
            conteo += 1

    def mostrarCola(self,cola):
        for elemento in cola:
            print("<<--------Cliente------->>")
            print(elemento.datos.cliente)
            print("<<---------Pizza-------->>")
            print(elemento.datos.pizza)
            print("--------------------------\n")


    # pop
    def desencolar(self):
        contador = 0
        temp = self.cabeza
        if self.cabeza is None:
            print("Lista vacia")
        else:
            while temp:
                if temp.siguiente is None:
                    break
                temp = temp.siguiente
            self.eliminar_pos(contador)
        return temp

    # devuelve el tamaño de la cola
    def get_length(self):
        contador = 0
        iterador = self.cabeza
        while iterador:
            contador += 1
            iterador = iterador.siguiente
        return contador

    def __iter__(self):
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente
