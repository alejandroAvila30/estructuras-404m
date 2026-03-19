


num_lotes = int(input("Cuantos lotes hay: "))
lote = 1

while True:
    print("\nLote", lote)


    agua = input("El riego esta bien? (si - no): ")
    fertilizacion = input("La fertilizacion esta bien? (si - no): ")
    plaga = input("Hay control de plagas? (si - no): ")


    if agua == "si" and fertilizacion == "si" and plaga == "si":
        print("El cultivo esta bien, pasando al siguiente lote")
    else:
        print("Se aplica riego, fertilizante o control de plaga")


    if lote == num_lotes:
        print("Ultimo lote, regresando al lote 1")
        lote = 1
    else:
        lote = lote + 1

    seguir = input("Continuar? (si - n): ")
    if seguir == "n":
        print("Proceso terminado")
        break
    
    #_____________________________________________________-
    
    

num_grupos = int(input("Cuantos grupos de recolectores hay: "))
num_zonas = int(input("Cuantas zonas hay: "))


grupos = []
for i in range(num_grupos):
    grupos.append("Grupo " + chr(65 + i))

grupo_index = 0
zona = 1

while zona <= num_zonas:
    print("\nZona", zona)


    grupo_actual = grupos[grupo_index % num_grupos]
    print("Se asigna:", grupo_actual)

    print(grupo_actual, "recolectando cafe en la zona", zona)

    print("Transportando cafe")


    if zona < num_zonas:
        print("Quedan zonas por recoger, asignando siguiente grupo")
        grupo_index = grupo_index + 1
        zona = zona + 1
    else:
        print("No quedan zonas, volviendo al", grupos[0])
        grupo_index = 0

        seguir = input("Iniciar nuevo ciclo? (s/n): ")
        if seguir == "s":
            zona = 1
        else:
            print("Recoleccion terminada")
            break
        
        #_____________________________________________________-
        
class Nodo:
    def __init__(self,cafe):
        self.cafe=cafe
        self.siguiente=None
        self.anterior=None


class Cafe:
    def __init__(self, despulpado, lavado, secado):
        self.despulpado = despulpado
        self.lavado = lavado
        self.secado = secado
        
        self.cabeza=None
        self.cola=None

    def LlenarLista(self,cantidadCafe):
        while cantidadCafe > 0:
            cantidadCafe -= 1
            CafeActual = Nodo(Cafe(False,False,False))

            if self.cabeza is None:
                self.cabeza = CafeActual
                self.cola = CafeActual
                self.cola.siguiente = self.cabeza
                self.cabeza.anterior = self.cola
            else:
                self.cola.siguiente = CafeActual
                CafeActual.anterior = self.cola
                self.cola = CafeActual
                self.cola.siguiente = self.cabeza
                self.cabeza.anterior = self.cola



def Despulpado(cafe):
    cafe.despulpado=True

def Lavado(cafe):
    cafe.lavado=True

def Secado(cafe):
    cafe.secado=True


# MAIN
cantidadCafe = int(input("Ingrese la cantidad de bultos de cafe: "))

lista = Cafe(False, False, False)
lista.LlenarLista(cantidadCafe)

actual = lista.cabeza
cont = 0

while cont < cantidadCafe:
    print(f"\n Café {cont+1}")

    Despulpado(actual.cafe)
    print(" Despulpado...")

    Lavado(actual.cafe)
    print(" Lavado...")

    Secado(actual.cafe)
    print(" Secado...")

    actual = actual.siguiente
    cont += 1

print("\n FIN")

#_____________________________________________________-

import random   

class Nodo:
    def __init__(self,cafe):
        self.cafe=cafe
        self.siguiente=None
        self.anterior=None


class Cafe:
    def __init__(self, peso, sellar, etiqueta):
        self.peso = peso
        self.sellar = sellar
        self.etiqueta = etiqueta
        
        self.cabeza=None
        self.cola=None

    def LlenarLista(self,cantidadCafe):
        while cantidadCafe > 0:
            cantidadCafe -= 1
            CafeActual = Nodo(Cafe(0,False,None))

            if self.cabeza is None:
                self.cabeza = CafeActual
                self.cola = CafeActual
                self.cola.siguiente = self.cabeza
                self.cabeza.anterior = self.cola
            else:
                self.cola.siguiente = CafeActual
                CafeActual.anterior = self.cola
                self.cola = CafeActual
                self.cola.siguiente = self.cabeza
                self.cabeza.anterior = self.cola


def Peso(cafe):
    cafe.peso = random.randint(490, 510)
    print(f"Peso real: {cafe.peso} gramos")

def Sellar(cafe):
    cafe.sellar = True
    
def Etiqueta(cafe):
    cafe.etiqueta = random.choice(["Arabica ", "Robusta", "Libérica y Excelsa"])
    print(f"Es cafe: {cafe.etiqueta}")
    
cont=0
cantidadCafe = int(input("Ingrese la cantidad de libras de cafe a producir: "))

lista = Cafe(0, False, None)
lista.LlenarLista(cantidadCafe)

actual = lista.cabeza
cont = 0

while cont < cantidadCafe:
    print(f"\n Libra de café {cont+1}")

    Peso(actual.cafe)
    
    
    Sellar(actual.cafe)
    print("Sellado...")
  
    
    Etiqueta(actual.cafe)
  
    

    actual = actual.siguiente
    cont += 1

print("\n FIN")

#______________________________________________________



rutas = ["Ruta 1", "Ruta 2", "Ruta 3", "Ruta 4"]
indice_ruta = 0

inventario = 10
pedidos = []

def mostrar_menu():
    print("\n--- SISTEMA DE PEDIDOS Y DISTRIBUCIÓN ---")
    print("1. Crear pedido")
    print("2. Ver pedidos")
    print("3. Procesar pedidos")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if inventario <= 0:
            print(" No hay inventario disponible")
            continue

        nombre = input("Nombre del cliente: ")
        pedido = {
            "cliente": nombre,
            "pago": False,
            "estado": "Pendiente"
        }

        confirmar = input("¿Pago confirmado? (si/no): ").lower()
        if confirmar == "si":
            pedido["pago"] = True
            

        pedidos.append(pedido)
        print(" Pedido registrado")

    elif opcion == "2":
        print("\n--- LISTA DE PEDIDOS ---")
        if not pedidos:
            print("No hay pedidos")
        for i, p in enumerate(pedidos):
            print(f"{i+1}. Cliente: {p['cliente']} | Estado: {p['estado']} | Pago: {p['pago']}")

    elif opcion == "3":
        for p in pedidos:
            if p["estado"] == "Pendiente" and p["pago"]:

                print(f"\nProcesando pedido de {p['cliente']}")

                
                ruta_actual = rutas[indice_ruta]
                print(f" Asignando {ruta_actual}")

                indice_ruta = (indice_ruta + 1) % len(rutas)

                print("Cargando pedido...")
                print("Distribuyendo...")

                for ruta in rutas:
                    print(f"Pasando por {ruta}")

                inventario -= 1
                p["estado"] = "Enviado"

        print("✔ Procesamiento terminado")

    elif opcion == "4":
        print("Sistema finalizado")
        break

    else:
        print(" Opción inválida")
        
        #______________________________________________________
        

pedidos = []

def menu():
    print("\n--- SISTEMA DE ENTREGA ---")
    print("1. Registrar pedido")
    print("2. Ver pedidos")
    print("3. Procesar entrega")
    print("4. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cliente = input("Nombre del cliente: ")
        pedidos.append({
            "cliente": cliente,
            "estado": "En preparación",
            "intentos": 0
        })
        print(" Pedido registrado")

    elif opcion == "2":
        print("\n--- LISTA DE PEDIDOS ---")
        if not pedidos:
            print("No hay pedidos")
        for i, p in enumerate(pedidos):
            print(f"{i+1}. {p['cliente']} | Estado: {p['estado']} | Intentos: {p['intentos']}")

    elif opcion == "3":
        for p in pedidos:
            if p["estado"] != "Entregado":

                print(f"\nProcesando entrega de {p['cliente']}")
                print("Preparando...")
                print("Enviando...")

                respuesta = input("¿Entrega exitosa? (si/no): ").lower()

                if respuesta == "si":
                    p["estado"] = "Entregado"
                    print(" Entrega completada")
                else:
                    p["intentos"] += 1
                    p["estado"] = "Reintento"
                    print("⚠ Se reintentará la entrega")

        print("✔ Proceso de entregas finalizado")

    elif opcion == "4":
        print("Sistema finalizado")
        break

    else:
        print(" Opción inválida")