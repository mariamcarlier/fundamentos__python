"""Las tuplas son secuencias inmutables, que normalmente se utilizan para
almacenar colecciones de datos heterogéneo. Las tuplas también se
utilizan para casos en los que se necesita una secuencia inmutable de
datos homogéneos.""" 
#TUPLA

# Estructura de una tupla:
tupla = ( "elemento1", "elemento2", "elemento3", "elemento4", "elemento5" )
print(type(tupla)) #<class 'tuple'>

tupla_2 = "a" , "b" , "c" , "d" , "e" 
#tambien se puede crear una tupla sin usar parentesis, pero es recomendable usarlo para evitar confusiones
print(type(tupla_2)) #<class 'tuple'>

tupla_3 = ("Hola")
print(type(tupla_3)) #<class 'str'> - esto se debe a que al crear una tupla con un solo elemento, es necesario incluir una coma después del elemento para que Python lo reconozca como una tupla. Sin la coma, Python interpreta el paréntesis como parte de la sintaxis de agrupación y no como una tupla. Por lo tanto, para crear una tupla con un solo elemento, se debe escribir: tupla_3 = ("Hola",)

tupla_4 = tuple("Hola")
print(tupla_4) # ('H' ,'o', 'l' , 'a')

tuplas_mixta = ("Hola", 123 , 3.4 , True , [1,2,3])
print(tuplas_mixta)

#TUPLA APRENDICES ADSO
#Indice:         0              1           2         3           4        5 
aprendices = ("Daniela" , "Estefania" , "Samara" , "Eliana" , "Valeria" , "Saira")
print(aprendices)

#ACCEDER A UN ELEMENTO DE LA TUPLA
print(aprendices[2]) #Samara

#Modificar un elemento de la tupla
#aprendices[2] = "Daniel" - esto generara un ERROR 

#Consultar rangos de elementos de la lista
# se muestra desde el indice 0 hasta el indice 1, el indice 2 no se incluye
print(aprendices[0:2]) 
# el : antes de un numero significa que se muestra desde el inicio hasta el indice que se indique, en este caso el indice 2 no se incluye
print(aprendices[:2]) 
# se muestra desde el indice 2 hasta el indice 3, el indice 4 no se incluye
print(aprendices[2:4])

# en este caso (: despues) inicia desde el indice 2 hasta el final de la lista 
print(aprendices[2:])   #('Samara', 'Eliana', 'Valeria', 'Saira')
print(aprendices[:])    #se muestra todo 
print(aprendices[2:5])  # ('Samara', 'Eliana', 'Valeria')
print(aprendices[-1])   # ultimo = Saira
print(aprendices [0::2])# pares = ('Daniela', 'Samara', 'Valeria')

# -------------------------------------------------------------------------
# Metodos de las tuplas

#Medir el largo con lent()
print(len(aprendices)) # 6

#Contar elementos repetidos con una tupla con count
print(aprendices.count("Valeria")) #1

#Obtener el indce de un elemento con index
print(aprendices.index("Samara")) #2

# -------------------------------------------------------------------------
#Modificar una tupla en una lista

print(type(aprendices)) #<class 'tuple'> 
aprendices_lista = list(aprendices) #😎Convertimos la tupla a una lista
print(type(aprendices_lista)) #<class 'list'>

aprendices_lista.append("Jennifer") #se agrego un elemento al final
print(aprendices_lista)

# hacer el proceso inverso = ahora se convierte la lista creada de nuevo en  tupla
aprendices = tuple(aprendices_lista)

# -------------------------------------------------------------------------
#comprobar pertenencia (in)
print("Daniela" in aprendices) #True
print("Camilo" in aprendices) #False

# -------------------------------------------------------------------------
# Empaquetar  tuplas

programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "Topografia"

tupla_programas = (programa_1, programa_2 , programa_3)
print(tupla_programas) #('ADSO', 'SST', 'Topografia')

#Desempaquear tuplas

tupla_desempaquetada = ('ADSO', 'SST', 'Topografia')
programa_1 , programa_2 , programa_3 = tupla_desempaquetada


# Ejercicio 2 - Desempaquetar TUPLAS
tupla_ciudades = ("Bogotá", "Medellín", "Cali")
ciudad_1 , *ciudad_2 =tupla_ciudades

print(ciudad_1)
print(ciudad_2)

#Iterar sobre una tupla con un ciclo for
for ciudad in tupla_ciudades:
    print(ciudad)

