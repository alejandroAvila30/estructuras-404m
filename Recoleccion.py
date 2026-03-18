
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