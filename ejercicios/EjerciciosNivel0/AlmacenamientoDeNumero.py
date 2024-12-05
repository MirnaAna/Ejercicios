# 3 almacene un número en una variable y pida al usuario adivinarlo

numero_secreto= 13
adivina= int(input("Adivina el número: "))

# si el usuario adivina correctamente el número, imprima un mensaje de felicitación

if adivina == numero_secreto:
    print("¡Felicidades! Has adivinado correctamente el número.")
else:
    print("Lo siento,te has equivocado, inténtalo de nuevo")