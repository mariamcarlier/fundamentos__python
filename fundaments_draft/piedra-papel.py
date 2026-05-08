#TRABAJO INTERACTIVO- ejercicio piedra papel o tijera
#CON INPUT - OPERADORES DE ASIGNACION - ARITMETICOS - COMPARACION -SENTENCIAS: IF, ELIF, ELSE - PRINT() 
# si es posible- F-STRINGS - FUNCION ROUND() - OPERADOR TERNARIO

#se importo la liberia random para que la computadora eliga una opcion al azar
import random

from flask.cli import F
print("=" * 65)
opciones = ["piedra", "papel", "tijera"]
print ("Bienvenido al juego: Piedra🪨 , Papel🗞️ o Tijera✂️")
print("Elige tu opción y compite contra la computadora. ¡Buena suerte!🍀") 
print("=" * 65)

#se creo un bucle infito con while true
while True:
    jugador = input("Elige una opcion😎: piedra, papel, tijera: ").lower() #se convirtio a minuscula para que el programa no tenga problemas con las mayusculas
    if jugador not in opciones: #si no es una de las opciones -se genera una opcion invalida
        print("Opcion invalida - Intente de nuevo...")
        continue #para que se aloje al siguente ciclo del bucle

    computadora = random.choice(opciones )#hace que la computadora eliga aleatoriamente en las opciones de lista
    print(f"La computadora elige🥁: {computadora}" )

    if jugador == computadora:
        print("¡¡EMPATE😯!!")
    elif (jugador == "piedra" and computadora == "tijera"):
        print("¡¡GANASTE🎉!!")
    elif (jugador == "papel" and computadora == "piedra"):
        print("¡¡GANASTE🎉!!")
    elif    (jugador == "tijera" and computadora == "papel"):
        print("¡¡GANASTE🎉!!")
    else:
        print("¡¡PERDISTE😢!!")
              
    continuar = input("¿Quieres jugar de nuevo? (1= si /2= no): ")
    if continuar != "1":
        print("Gracias por jugar, ¡hasta la próxima!👋")
        break
