#EJERCICIO 1 - 
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.
#producto = suma
print("="*75)
print("Ejercicio 1: 🧮Producto Escalar de Vectores en Tuplas📐")
print("="*75)
vectores_1 = (1,2,3)
vectores_2 = (-1,0,2)

producto_escalar = vectores_1, vectores_2
print(sorted(producto_escalar))

# EJERCICIO 2 -
#Escribir un programa que almacene en una tupla los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
print("="*75)
print("Ejercicio 2: 📊Menor y Mayor de los Precios")
print("="*75)

precios = (50, 75, 46, 22, 80, 65, 8)
print(f"El menor precio es: {min(precios)}")
print(f"El mayor precio es: {max(precios)}")

#de otra forma
precios_ordenados = sorted(precios)
print(precios_ordenados[0])
print(precios_ordenados[-1])