#REFERENCIA DE OPERADORES - Diap: 31
#OPERADORES ARITMETICOS 
tipo_operacion = int (input("Ingrese la operación que desea realizar "
"(1. suma, 2. resta, 3. multiplicación, 4. división): "))

valor1 = float (input("Ingrese el primer número: "))
valor2 = float (input("Ingrese el segundo número: "))

if tipo_operacion == 1:
    resultado = valor1 + valor2
    print(f"Suma: {resultado}")

if tipo_operacion == 2:
    resultado = valor1 - valor2
    print(f"Resta: {resultado}")

if tipo_operacion == 3:
    resultado = valor1 * valor2
    print(f"Multiplicación: {resultado}")

if tipo_operacion == 4:
    if valor2 != 0:
        resultado = valor1 / valor2
        print(f"División: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")


suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2    
division = valor1 / valor2
division_entera = valor1 // valor2
modulo = valor1 % valor2
exponenciacion = valor1 ** valor2

"""
print(f"Suma:{suma}")
print(f"Resta:{resta}")
print(f"Multiplicación:{multiplicacion}")
print(f"División:{division}")
print(f"División entera:{division_entera}")
print(f"Módulo:{modulo}")
print(f"Exponenciación:{exponenciacion}")
"""


#RETO:
#1. Crear un programa que solicite al usuario dos números enteros y realice las operaciones aritméticas básicas (suma, resta, multiplicación, división) con esos números. Mostrar los resultados de cada operación.

opcion1 = int (input("Ingrese el primer número: "))
opcion2 = int (input("Ingrese el segundo número: "))

print( tipo_operacion)