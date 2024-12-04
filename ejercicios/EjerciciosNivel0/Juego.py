#  Crea un juego para jugar contra la computadora al juego de «Piedra, papel o tijera».
import random

Eljuego = {
    "piedra": ["tijera"],
    "papel": ["piedra"],
    "tijera": ["papel"]
}

while True:
    eleccion = random.choice(list(Eljuego.keys())) 
    eleccion_user = input("Elige piedra, papel o tijera: ").lower()

    if eleccion_user == 'salir':
        print("Gracias por jugar")
        break
    print(f'La máquina saca {eleccion} y tú sacas {eleccion_user}')
    
    if eleccion_user not in Eljuego:
        print("Elección inválida")
        continue
    
    if eleccion_user == eleccion:
        print("Es un empate")
    elif eleccion_user in Eljuego[eleccion]:  
        print('Win')
    else:
        print('Lose')