
class Orden:
    def __init__(self, entrada, plato_fuerte, bebida):
        self.entrada = entrada
        self.plato_fuerte = plato_fuerte
        self.bebida = bebida

    def mostrar(self, mesa):
        print("___________________________")
        print(f"Mesa: {mesa}")
        print(f"Entrada: {self.entrada}")
        print(f"Plato fuerte: {self.plato_fuerte}")
        print(f"Bebida: {self.bebida}")
        print("___________________________")


class NodoDoble:
    def __init__(self, orden):
        self.orden = orden
        self.siguiente = None
        self.anterior = None



class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, orden):
        nuevo = NodoDoble(orden)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def recorrer(self, mesa):
        actual = self.cabeza
        i = 1
        if actual is None:
            print("No hay órdenes para esta mesa")
            return

        while actual:
            print(f"Orden #{i}")
            actual.orden.mostrar(mesa)
            actual = actual.siguiente
            i += 1

    def obtener(self, indice):
        actual = self.cabeza
        i = 0
        while actual:
            if i == indice:
                return actual.orden
            actual = actual.siguiente
            i += 1
        return None

    def eliminar(self, indice):
        actual = self.cabeza
        i = 0
        while actual:
            if i == indice:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
            i += 1
        return False

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.ordenes = ListaDoble()

class Mesero:
    def __init__(self, mesas):
        self.mesas = mesas

        self.entradas = {
            1: "Crema de champiñones",
            2: "Dedos de queso",
            3: "Sopa de verduras"
        }
        self.platos = {
            1: "Hamburguesa especial de la casa",
            2: "Arroz con pollo",
            3: "Chuleta de cerdo"
        }
        self.bebidas = {
            1: "Limonada",
            2: "Jugo de fresa",
            3: "Gaseosa"
        }

    def seleccionar(self, opciones, titulo):
        print(f"\n{titulo}")
        for k, v in opciones.items():
            print(f"{k}. {v}")
        while True:
            try:
                op = int(input("Seleccione: "))
                if op in opciones:
                    return opciones[op]
                else:
                    print("Opción inválida")
            except ValueError:
                print("Debe ingresar un número")

    def agregar_orden(self):
        try:
            mesa = int(input("Mesa (1-5): "))
            if mesa not in self.mesas:
                print("Mesa inválida")
                return
        except ValueError:
            print("Entrada inválida")
            return

        entrada = self.seleccionar(self.entradas, "ENTRADAS")
        plato = self.seleccionar(self.platos, "PLATOS FUERTES")
        bebida = self.seleccionar(self.bebidas, "BEBIDAS")

        self.mesas[mesa].ordenes.agregar(
            Orden(entrada, plato, bebida)
        )
        print(" Orden agregada correctamente")

    def editar_orden(self):
        try:
            mesa = int(input("Mesa: "))
            if mesa not in self.mesas:
                print("Mesa inválida")
                return
        except ValueError:
            print("Entrada inválida")
            return

        self.mesas[mesa].ordenes.recorrer(mesa)
        try:
            indice = int(input("Número de orden a editar: ")) - 1
        except ValueError:
            print("Entrada inválida")
            return

        orden = self.mesas[mesa].ordenes.obtener(indice)
        if orden:
            orden.entrada = self.seleccionar(self.entradas, "Nueva entrada")
            orden.plato_fuerte = self.seleccionar(self.platos, "Nuevo plato fuerte")
            orden.bebida = self.seleccionar(self.bebidas, "Nueva bebida")
            print(" Orden editada correctamente")
        else:
            print(" Orden no encontrada")

    def eliminar_orden(self):
        try:
            mesa = int(input("Mesa: "))
            if mesa not in self.mesas:
                print("Mesa inválida")
                return
        except ValueError:
            print("Entrada inválida")
            return

        self.mesas[mesa].ordenes.recorrer(mesa)
        try:
            indice = int(input("Número de orden a eliminar: ")) - 1
        except ValueError:
            print("Entrada inválida")
            return

        if self.mesas[mesa].ordenes.eliminar(indice):
            print(" Orden eliminada correctamente")
        else:
            print(" No se pudo eliminar la orden")


class Cocina:
    def __init__(self, mesas):
        self.mesas = mesas

    def mostrar_todo(self):
        print("\n ÓRDENES EN COCINA")
        for mesa in self.mesas.values():
            mesa.ordenes.recorrer(mesa.numero)



class SistemaRestaurante:
    def __init__(self):
        self.mesas = {i: Mesa(i) for i in range(1, 6)}
        self.mesero = Mesero(self.mesas)
        self.cocina = Cocina(self.mesas)

    def ejecutar(self):
        while True:
            print("\n===== RESTAURANTE =====")
            print("1. Cocina")
            print("2. Mesero")
            print("3. Salir")

            op = input("Seleccione una opción: ")

            if op == "1":
                self.cocina.mostrar_todo()

            elif op == "2":
                while True:
                    print("\n----- MESERO -----")
                    print("1. Agregar orden")
                    print("2. Editar orden")
                    print("3. Eliminar orden")
                    print("4. Atrás")

                    o = input("Seleccione una opción: ")

                    if o == "1":
                        self.mesero.agregar_orden()
                    elif o == "2":
                        self.mesero.editar_orden()
                    elif o == "3":
                        self.mesero.eliminar_orden()
                    elif o == "4":
                        break
                    else:
                        print("Opción inválida")

            elif op == "3":
                print(" Saliendo del sistema")
                break
            else:
                print("Opción inválida")



SistemaRestaurante().ejecutar()