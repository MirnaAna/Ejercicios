# 9  Genera un número aleatorio entre 1 y 100. Luego, pide al usuario que 
# adivine el número y da pistas si el número ingresado es mayor o menor que el número secreto.

import random
 # Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False
print("¡Adivina el número secreto del 1 al 100!")
while not adivinado:
        num = int(input("Ingresa un número: "))
        intentos += 1
        if num == numero_secreto:
            adivinado = True
        elif num < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")
print(f"¡Bien! Adivinaste el número:{numero_secreto} en {intentos} intentos.")