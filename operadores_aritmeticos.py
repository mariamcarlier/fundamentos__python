# OPERADORES ARITMETICOS
a = 3
b = 2

#SUMA 
suma = a + b
print(f" La Suma de {a} y {b} es: {suma}")

#RESTA
resta = a - b
print(f" La Resta de {a} y {b} es: {resta}")

#MULTIPLICACION
multiplicacion = a * b  
print(f" La Multiplicación de {a} y {b} es: {multiplicacion}")  

#DIVISION - flotante o decimal
division = a / b
print(f" La División de {a} y {b} es: {division}")

#DIVISION ENTERA - quita los decimales y muestra solo la parte entera del resultado de la division
division_entera = a // b
print (f"La division entera de {a} y {b} es : {division_entera}")

#MODULO(residuo)
modulo = a % b
print(f" El Modulo de {a} y {b} es: {modulo}")

#EXPONENCIACION **
exponenciacion = a ** b
print(f" La Exponenciación de {a} y {b} es: {exponenciacion}")

#PRECEDENCIA DE OPERADORES #- orden de prioridad en el que se ejecutan los operadores en una expresión matemática. La precedencia de operadores determina el orden en el que se evalúan los operadores en una expresión, lo que puede afectar el resultado final de la expresión. En Python, la precedencia de operadores es la siguiente:

resultado_1 = a + b * 2 
print (f" El resultado de la expresion {a} + {b} * 2 es: {resultado_1}")
#EN ESTE CASO, SE REALIZA PRIMERO LA MULTIPLICACION ENTRE b Y 2, Y LUEGO SE SUMA EL RESULTADO A a, POR LO QUE EL RESULTADO FINAL DE LA EXPRESION ES 7.

resultado_2 = (a + b) * 2
print (f" El resultado de la expresion ({a} + {b}) * 2 es: {resultado_2}")
#EN ESTE CASO, SE REALIZA PRIMERO LA SUMA ENTRE a Y b, Y LUEGO SE MULTIPLICA EL RESULTADO POR 2, POR LO QUE EL RESULTADO FINAL DE LA EXPRESION ES 10.

resultado_3 = a* b // 3
print (f" El resultado de la expresion {a} * {b} // 3 es: {resultado_3}")
#EN ESTE CASO, SE REALIZA PRIMERO LA MULTIPLICACION ENTRE a Y b, Y LUEGO SE REALIZA LA DIVISION ENTERA ENTRE EL RESULTADO DE LA MULTIPLICACION Y 3, POR LO QUE EL RESULTADO FINAL DE LA EXPRESION ES 2.

resultado_4 = (a+b) // 3
print (f" El resultado de la expresion ({a} + {b}) // 3 es: {resultado_4}")
#EN ESTE CASO, SE REALIZA PRIMERO LA SUMA ENTRE a Y b, Y LUEGO SE REALIZA LA DIVISION ENTERA ENTRE EL RESULTADO DE LA SUMA Y 3, POR LO QUE EL RESULTADO FINAL DE LA EXPRESION ES 1.

resultado_5 = a* (b // 3)
print (f" El resultado de la expresion {a} * ({b} // 3) es: {resultado_5}")
#EN ESTE CASO, SE REALIZA PRIMERO LA DIVISION ENTERA ENTRE b Y 3, Y LUEGO SE MULTIPLICA EL RESULTADO POR a, POR LO QUE EL RESULTADO FINAL DE LA EXPRESION ES 0.



#planteamiento de un ejercicio aplicando esta jerarquia con su orden (precedencia ) :
ejercicio_practica = ((a + b )* (a - b ) / (a * b)) - ((a**b) % 3 )
    #paso a paso : (3+2) * (3-2) / (3*2) - ((3**2) % 3 ) 
    #               = 5 * 1 / 6 - (9 % 3 ) 
    #                   = 5 / 6 - 0 = 0.8333333333333334

print (f" El resultado de la expresion (({a} + {b} )* ({a} - {b} ) / ({a} * {b})) - (({a}**{b}) % 3 ) es: {ejercicio_practica}")


# Librerias 
# - buenas practicas en el codigo seria siempre importar las librerias al inicio del codigo, para que el codigo sea mas organizado y facil de leer, ademas de que si se necesita utilizar una libreria en varias partes del codigo, no se tendria que importar la libreria varias veces, sino que se importaria una sola vez al inicio del codigo y se podria utilizar en cualquier parte del codigo.- Basicamente por que PYTHON ES UN LENGUAJE SECUENCIAL (CASCADA) - por lo que el codigo se ejecuta de arriba hacia abajo, si se importa una libreria en medio del codigo, la libreria solo estaria disponible a partir de ese punto en adelante, por lo que si se intenta utilizar la libreria antes de importarla, se generaria un error. Por eso es importante importar las librerias al inicio del codigo para evitar errores y tener un codigo mas organizado y facil de leer.

import math

print(math.pi) 
print(math.e)
print(math.sqrt(16)) # raiz cuadrada de 16, el resultado es 4.0, ya que la funcion sqrt() devuelve un numero decimal (float) aunque el resultado sea un numero entero, por eso el resultado es 4.0 y no 4.

import random
random.random() # devuelve un numero decimal aleatorio entre 0 y 1, por ejemplo: 0.12345678901234567

numero_aleatorio = random.randint(1, 10) # devuelve un numero entero aleatorio entre 1 y 10, por ejemplo: 7
print(numero_aleatorio)


