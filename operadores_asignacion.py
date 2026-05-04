# Operadores de asignacion
# Los operadores de asignacion se utilizan para asignar un valor a una variable. El operador de asignacion mas comun es el signo igual (=), que se utiliza para asignar un valor a una variable. 

# el operador (-=) / (+=) / (*=) / (/=) / (%=) / (**=) se utiliza para realizar la operacion correspondiente y asignar el resultado a la misma variable, lo que permite escribir codigo mas conciso y facil de leer. - ES UNA BUENA PRACTICA  

# Por ejemplo:
# 1 suma y asignacion (+=)
x = 5
print (x) 
x = x + 2
x += 2 #esta es una forma mas corta de escribir x = x + 2, el operador += se utiliza para sumar un valor a una variable y asignar el resultado a la misma variable. En este caso, se suma 2 a x y se asigna el resultado a x, por lo que el valor de x ahora es 9.
print (x)

# 2 resta y asignacion (-=)
x =  x - 3
x-= 3
print (x) 

# 3 Multiplicacion y asignacion
x = x * 4
x*= 4
print (x)

# 4 Division y asignacion (/=)
x = x / 2
x/= 2
print (x)


# PARA EVITAR LA FATIBA DE LINEAS DE CODIGO -tip: caracter especial := la idea es que dentro de una funcion se pueda hacer una asignacion de variable y al mismo tiempo utilizar esa variable en la misma funcion, sin necesidad de escribir una linea de codigo adicional para asignar el valor a la variable antes de utilizarla. (:= Operador WALRUS)
# EJEMPLO DE USO DE OPERADOR WALRUS (nos damos cuenta que la variable puede cambiar su valor)
print ( x := 10 ) # Asigna 10 a  la variable x y luego imprime x
