# condicional 
if False:
    print("la primera condicion es verdadera")
elif False:
    print("La segunda condicion es verdadera en ELIF")
elif False:
    print("la tercera condicion es verdadera en elif")
else :
    print("la condicion es falsa")


#Ejercicio en clasificacion de Edad
edad = 18

if edad < 18: #Si
    print("Eres un menor de edad")
elif edad >= 18 and edad < 65: # sino
    print("Eres un adulto")
else: #entonces
    print("Eres un adulto mayor")

#Ejercicio en clasificacion de Edad if ANIDADO
edad = int(input("Ingrese su Edad para ser clasificada:"))

if edad < 18:
    if edad > 12 and edad < 18: #si es menor que 12 y mayor de 18 es adolesente
        print ("Eres Adolecente ")
    else:
        print("Eres un Niño")
else:
    if edad >=26 and edad <40: # si es mayor o igual a 26 y menor que 40 entonces es adulto
        print("Eres un adulto")
    else:
        print("Eres un adulto mayor")# sino es adulto mayor

#Concepto- operador ternario - entre menos lineas sera mas optimizado-simplifica 4 lineas en una
#sintaxis :[true] if [expresion] else [false]
numero = 4
print("El número es par") if numero % 2 == 0 else print("El número es impar")

#PARTE LARGA
#if numero %2 == 0:
#   print("El numero es par")
#else:
    #print ("el numero es impar")
