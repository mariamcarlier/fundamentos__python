#LISTAS Y SU ESTRUCTURA
#Indice 0      1      2      3
listas = ['objeto_1', 'objeto_2', 'objeto_3', 'objeto_4']
print(type(listas)) # class 'list'>

#yo puedo guardar una lista con diferentes tipos de datos , asi: 
#Son heterogéneas porque pueden almacenar diferentes tipos de objetos.
lista_mixta = ['Hola', 99 , 0.36 , True,[1,2,3]]

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

aprendices_ficha_3321349 =['Alejandra' ,'Giselle', 'Daniel', 'Laura', 'Stiven', 'Miguel', 'Sebastian','Stephanie','Mario', 'Luis']
aprendices_ficha_2993648 = ['Alejandra','Sofia', 'Andres', 'Valentina', 'Camilo', 'Sara', 'Yuri', 'Diana', 'Jorge', 'Santiago', 'Maria']

# concatenar listas
aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_2993648
print(aprendices_adso)

# unir listas con extend
aprendices_ficha_3321349.extend(aprendices_ficha_2993648)
print(aprendices_ficha_3321349)

#medir el largo con lent
longuitud_adso =(len(aprendices_adso)) #len= longuitud 21 registros
print(f"La lista de aprendices adso tiene {longuitud_adso} elementos.")

#countar elementos con count 
#dice cuandas veces se repite un elemento en la lista

count_aleja = aprendices_adso.count('Alejandra') #2
print(f"El nombre 'Alejandra' se repite {count_aleja} veces en la lista.")

#obtener el indice de un elemento con index
indice_sara = aprendices_adso.index('Sara') #5
print(f"El nombre 'Sara' se encuentra en el índice {indice_sara} de la lista.")

#copiar lista con copy - es como ctrl v +c
nueva_lista_adso =aprendices_adso.copy()
print(nueva_lista_adso)

#Agregar elementos con append - agrega un elemento al final de la lista 
#y insert - agrega un elemento en una posición específica de la lista
nueva_lista_adso.append("Falcao")
nueva_lista_adso.insert(1, "James")
print(nueva_lista_adso)

#eliminar elementos (remove -pop)
#pop- elimina y devuelve un elemento (por indice o ultimo)
#remove - Elima la primera ocurrencia de un valor
nueva_lista_adso.remove("Stiven")
print(nueva_lista_adso)

nueva_lista_adso.pop(11)#elimina a sofia
print(nueva_lista_adso)

#comprobar pertinencia (in)
if "Mesi" in nueva_lista_adso:
    print("Si se encuentra registrado")    
else:
  print("Ese nombre/registro NO se encuentra en lista")

  #ordenar lista (sort y reverse)
nueva_lista_adso.sort() # ordena la lista de forma ascendente (alfabeticamente)
print(nueva_lista_adso)
nueva_lista_adso.reverse() # ordena la lista de forma descendente (alfabeticamente)
print(nueva_lista_adso)

#ELIMINAR TODOS LOS ELEMENTOS DE UNA LISTA
nueva_lista_adso.clear()
print(nueva_lista_adso) # se muestra una lista vacia []
