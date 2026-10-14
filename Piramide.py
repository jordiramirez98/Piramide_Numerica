
N = int(input("Ingrese un número del 1 al 9: "))

if N >= 1 and N <= 9:
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
else:
    print("Ingrese un numero valido")



