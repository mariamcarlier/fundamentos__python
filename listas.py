#LISTAS Y SU ESTRUCTURA
#Indice 0      1      2      3
listas = ['objeto_1', 'objeto_2', 'objeto_3', 'objeto_4']
print(type(listas)) # class 'list'>

#yo puedo guardar una lista con diferentes tipos de datos , asi: 
#Son heterogéneas porque pueden almacenar diferentes tipos de objetos.
lista_mixta = ['Hola', 99 , 0.36 , True]

#crear una lista de aprendices
aprendices = ['Mariam', 'Sharyt', 'Camilo', 'Simon', 'David']
print(aprendices)

#Acceder a un elemento de la lista
print(aprendices[0])  # Accede al primer elemento
print(aprendices[3])  # Accede al cuarto elemento

#Modificando un Elemento de la lista
aprendices[2] = "Ivan"
print(aprendices)

#Consultar rangos de elementos de la lista
print(aprendices[0:2]) # se muestra desde el indice 0 hasta el indice 1, el indice 2 no se incluye
print(aprendices[:2]) # el : antes de un numero significa que se muestra desde el inicio hasta el indice que se indique, en este caso el indice 2 no se incluye
print(aprendices[2:4])# se muestra desde el indice 2 hasta el indice 3, el indice 4 no se incluye
print(aprendices[2:]) # en este caso (: despues) inicia desde el indice 2 hasta el final de la lista 
print(aprendices[:])# se muestra toda la lista - ['Mariam', 'Sharyt', 'Ivan', 'Simon', 'David']
print(aprendices[2:5]) #['Ivan', 'Simon', 'David']

print(aprendices[-1]) # se muestra el ultimo elemento de la lista, en este caso 'David'
print(aprendices [0::2]) # se muestra desde el indice 0 hasta el final de la lista, pero solo los elementos que estan en los indices pares, en este caso 'Mariam', 'Ivan' y 'David'

aprendices_ficha_3321349 =['Giselle', 'Daniel', 'Laura', 'Stiven', 'Miguel', 'Sebastian','Stephanie','Mario', 'Luis']
aprendices_ficha_2993648 = ['Sofia', 'Andres', 'Valentina', 'Camilo', 'Sara', 'Yuri', 'Diana', 'Jorge', 'Santiago', 'Maria']

# concatenar listas
aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_2993648
print(aprendices_adso)