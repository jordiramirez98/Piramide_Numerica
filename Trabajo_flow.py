opcion_general = 0

# Ciclo principal para mantener el menú siempre activo hasta elegir salir
while opcion_general != 4:
    print("Menu ejercicios")
    print("1. Triángulo de números del 1 al 9")
    print("2. Separar 15 números en pares e impares")
    print("3. Encontrar números primos")
    print("4. Salir")
    
    opcion_general = int(input("Ingresa tu opción 1, 2, 3 o 4: "))
    
    #Triángulo de números
    if opcion_general == 1:
        print("\n--- 1. TRIÁNGULO DE NÚMEROS ---")
        numero_triangulo = int(input("Ingrese un número del 1 al 9: "))

        if numero_triangulo >= 1 and numero_triangulo <= 9:
            for fila in range(1, numero_triangulo + 1):
                for columna in range(1, fila + 1):
                    print(columna, end="")
                print() # Salto de línea
        else:
            print("Ingrese un numero valido.")

    # Primos
    elif opcion_general == 3:
        limite_p = int(input("Ingresa el valor hasta donde quiere contar los primos: "))
        cantidad_primos = 0
        
        print(f"Los números primos entre 1 y {limite_p} son:")
        
        for numero_actual in range(1, limite_p + 1):
            if numero_actual > 1:
                es_primo = True
                
                for divisor in range(2, numero_actual):
                    if numero_actual % divisor == 0:
                        es_primo = False
                        break
                
                if es_primo == True:
                    print(numero_actual, end=" ")
                    cantidad_primos += 1 
        print(f"Total de números primos encontrados: {cantidad_primos}")

    elif opcion_general == 4:
        print("Saliendo del programa. ¡Hasta luego!")

    else:
        print("\nOpción no válida, intente de nuevo.")