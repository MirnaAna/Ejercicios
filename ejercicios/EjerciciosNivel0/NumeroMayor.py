# 6  El usuario ingresa 2 números (pueden contener decimales) y el programa indica cuál de los dos es el mayor, o si son iguales.

numero1 = float(input("Ingresa un numero "))
numero2 = float(input("Ingresa otro numero "))
if numero1 > numero2:
    print("El primer numero es el mayor ", numero1)
elif numero1 < numero2:
    print("El segundo numero es el mayor ", numero2)