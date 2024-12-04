# 8 Escribe un programa que calcule el factorial de un número entero positivo ingresado por el usuario.

numero = int(input("Ingresa un numero entero positivo "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
    print("El factorial del numero ingresado es:", factorial)
