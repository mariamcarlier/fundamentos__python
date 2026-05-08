"""EJERCICIO 1 :crear las siguientes variables según su criterio:

• Una variable que permita almacenar el nombre de una persona.
• Una variable que permita almacenar un valor de un producto.
• Una variable que permita almacenar el promedio de una asignatura.
• Imprima en consola las variables creadas
"""
#------------------------------------------------------------------------------------
print("=" *69)
print("Este es el ejercicio 1")
nombre = "Amelie"
precio_producto = 35000
promedio_asignatura = 3.5
print(F"Hola {nombre}")
print(precio_producto)
print(promedio_asignatura)

#------------------------------------------------------------------------------------
print("=" *69)
"""EJERCICIO 2: Crear programa que lea tipos de datos y los relacione con operadores
introducidos por teclado : dos enteros, un float, dos String.

• Se deben sumar los tres número y se muestran en pantalla.
• Se debe visualizar el entero mayor.
• Se debe visualizar el resultado de la división del float con el resto de
la división de los dos enteros.
• Se debe visualizar la concatenación de las dos cadenas leídas.
"""
print("Este es el ejercicio 2")
numero_entero1 = int(input("Ingrese el primer número entero: "))
numero_entero2 = int(input("Ingrese el segundo número entero: "))
numero_float1= float(input("Ingrese un numero decimal flotante: (ej:3.6) :"))

ej_2_suma = numero_entero1 + numero_entero2 + numero_float1
print(f"La suma de las variables numericas es :{ej_2_suma} ")

if numero_entero1 > numero_entero2:
    print (f"El primer numero entero que ingreso es mayor = {numero_entero1}")
    
else:
    print (f"El segundo numero que ingreso es mayor = {numero_entero2}")   

variable_1_string = input("Ingrese la primera cadena de texto: ")
variable_2_string = input("Ingrese la segunda cadena de texto: ")
ej_2_texto = (variable_1_string) + " " +(variable_2_string)
print(f"La concatenacion de los textos ingresados es :{ej_2_texto}")

#------------------------------------------------------------------------------------
print("=" *69)
"""Ejercicio 3 -Condicionales:

Crear 2 variables enteras, una llamada “Base” y la otra “Exponente”,
asignar valores a su criterio. Calcular la potencia utilizando y mostrar el
resultado de la operación."""
print("Este es el ejercicio 3--- CALCULADORA DE potencia---🧠")

base = int(input("Ingrese el la base : "))
exponente = int(input("Ingrese el exponente  : "))

# 2. Calcular la potencia utilizando el operador **
resultado = base ** exponente

# 3. Mostrar el resultado de la operación
print(f"{base} elevado a la {exponente} es: {resultado}")

#------------------------------------------------------------------------------------
"""Ejercicio 4 -Condicionales

Hallar la raíz cuadrada de los siguientes números 2, 8, 9, 27, 28, 55, 121
y mostrar los resultados de cada operación. """
print("=" *69)
print("---Este es el ejercicio 4 - CALCULADORA DE RAIZ CUADRADA---🧠- ")

#usando la libreria math 
import math 
e_raiz_cuadrada = float(input( "Escribe el numero para calcular el resultado de su raiz cuadrada: "))

#verificar que el numero ingresado no es negativo
if e_raiz_cuadrada < 0:
    print("No se puede calcular la raiz cuadrada de un numero negativo en los reales.")
else:
    raiz= math.sqrt(e_raiz_cuadrada)
    print(f"La raiz cuadrada de {e_raiz_cuadrada} es: {raiz}")

#------------------------------------------------------------------------------------
print("=" *69)
"""Ejercicio 5

• Crear una variable para almacenar el nombre de un estudiante.
• Crear 5 variables para almacenar 5 diferentes notas decimales.
• Calcular el promedio final del estudiante a partir de las 5 notas
decimales. (Recuerda que un promedio se calcula sumando todos los valores y dividiendo el resultado por el número de valores).
• Mostrar el resultado y el nombre del estudiante."""


#------------------------------------------------------------------------------------
print("=" *69)
"""Ejercicio 6

Crear una variable entera de nombre “numeroUno” con el valor de 8 y
una variable entera de nombre “numeroDos” con el valor de 2.
Intercambiar los valores de ambas variables, de modo que
“numeroUno” valga 2, y

“numeroDos” valga 8. (Utiliza una variable

auxiliar). Mostrar los resultados de ambas variables."""

#------------------------------------------------------------------------------------
print("=" *69)
"""Ejercicio 7

Condicionales

Crear una variable booleana llamada “Estado”. Realizar la siguiente
operación sobre la variable “Estado”: (5 == 2) || (2 > 1). Mostrar el
resultado de la variable “Estado”."""
#------------------------------------------------------------------------------------
print("=" *69)
"""Ejercicio 8

Condicionales

• Crear una variable llamada “Resultado”.
• Dentro de la variable “Resultado”, crear una operación aritmética
donde se haga uso de todos los operadores matemáticos en
repetidas ocasiones con los números que tú determines.
• Ejemplo: (9/2) +8*2/1-(2+2) ....
• Mostrar el resultado de la operación."""

#------------------------------------------------------------------------------------
print("=" *69)
#EJERCICIO 9

#------------------------------------------------------------------------------------
print("=" *69)
#EJERCICIO 10