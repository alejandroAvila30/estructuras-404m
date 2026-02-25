def cuenta_regresiva(n):
    if n <= 0:
        print("BOMMMM")
    else:
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(3)
