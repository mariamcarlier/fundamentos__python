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

#PRECEDENCIA DE OPERADORES- orden de prioridad en el que se ejecutan los operadores en una expresión matemática. La precedencia de operadores determina el orden en el que se evalúan los operadores en una expresión, lo que puede afectar el resultado final de la expresión. En Python, la precedencia de operadores es la siguiente:

resultado_1 = a + b * 2 
print (f" El resultado de la expresion {a} + {b} * 2 es: {resultado_1}")
#EN ESTE CASO, SE REALIZA PRIMERO LA MULTIPLICACION ENTRE b Y 2, Y LUEGO SE SUMA EL RESULTADO A a, POR LO QUE EL RESULTADO FINAL DE LA EXPRESION ES 7.

resultado_2 = (a + b) * 2
print (f" El resultado de la expresion ({a} + {b}) * 2 es: {resultado_2}")
#EN ESTE CASO, SE REALIZA PRIMERO LA SUMA ENTRE a Y b, Y LUEGO SE MULTIPLICA EL RESULTADO POR 2, POR LO QUE EL RESULTADO FINAL DE LA EXPRESION ES 10.
