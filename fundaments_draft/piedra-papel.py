#TRABAJO INTERACTIVO- ejercicio piedra papel o tijera
#CON INPUT - OPERADORES DE ASIGNACION - ARITMETICOS - COMPARACION -SENTENCIAS: IF, ELIF, ELSE - PRINT() 
# si es posible- F-STRINGS - FUNCION ROUND() - OPERADOR TERNARIO

#se importo la liberia random para que la computadora eliga una opcion al azar
import random

#1. PRESENTACION DEL JUEGO:
print("= " * 45)
print("\n --🎮 PIEDRA , PAPEL O TIJERA 🎮-- ")
print("= " * 45)

#2. LISTA DE OPCIONES
#guardamos las posibles opciones en una lista
#-la utilizamos porque luego se utilizara random.choise() para elegir una alazar
opciones= ["piedra", "papel" , "tijera"]

#3. VARIABLES DE CONTROL
# se creo unas variables para almacenar el puntaje inicial o durante todo el juego
puntos_usuario = 0
puntos_pc = 0

#4 CONFIGURACION DEL JUEGO
#pedimos cuantas rondas desea jugar el usuario y se convirtio en entero para que se pueda utilizar la libreria de rango
rondas= int(input("¿ Cuantas rondas quieres jugar ? :"))

#5 BUCLE PRINCIPAL
#ESTE FOR CONTROLA CUANTAS VECES PUEDE REPETIRSE EL JUEGO
#range(rondas)- genera una secuencia de 0 a -1
for i in range(rondas):

    #mostramos el numero de la ronda (i+1 porque i empieza en 0)
    print(f"n-- RONDA{i+1}")

#6 ENTRADA DEL USUARIO
usuario = input("Elige (piedra, papel o tijera ): ") .lower()
#ese lower convierte todo a minusculas para evitar errores

# --VALIDACION
#Verificamos que la opción esté dentro de la lista
    # ¿Por qué? → para evitar errores o entradas inválidas
if usuario not in opciones:
    print("❌ Opción inválida")
    #5continue  # Salta a la siguiente ronda sin ejecutar lo demás


    # ====== ELECCIÓN DE LA COMPUTADORA ======
    # random.choice() selecciona un elemento aleatorio de la lista
    pc = random.choice(opciones)


    # Mostramos elecciones
    print(f"Tú elegiste: {usuario}")
    print(f"PC eligió: {pc}")


    # ====== LÓGICA DEL JUEGO ======
    # Aquí se decide quién gana

    # Caso 1: empate
    if usuario == pc:
        print("🤝 Empate")


    # Caso 2: gana el usuario
    # Se usan múltiples condiciones con "or"
    # Cada combinación representa una forma de ganar
    elif (
        (usuario == "piedra" and pc == "tijera") or
        (usuario == "tijera" and pc == "papel") or
        (usuario == "papel" and pc == "piedra")
    ):
        print("🎉 ¡Ganaste esta ronda!")

        # Operador de asignación +=
        # ¿Por qué? → suma 1 al puntaje actual
        puntos_usuario += 1


    # Caso 3: gana la computadora
    else:
        print("💻 La PC gana")
        puntos_pc += 1


# ====== RESULTADO FINAL ======
# Después del ciclo mostramos resultados

print("\n🏆 RESULTADO FINAL 🏆")
print(f"Tú: {puntos_usuario} | PC: {puntos_pc}")


# ====== DECISIÓN FINAL ======
# Comparamos puntajes para definir ganador total

if puntos_usuario > puntos_pc:
    print("🔥 ¡Eres el ganador!")

elif puntos_usuario < puntos_pc:
    print("😢 Perdiste contra la PC")

else:
    print("🤝 Empate total")