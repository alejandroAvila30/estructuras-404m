

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
