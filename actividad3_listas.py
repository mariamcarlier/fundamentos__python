print("="*75)
print("Actividad 3: 👩🏽🎤Gestión de Lista de Reproducción Musical🎼🎶")
print("="*75)

canciones = ['driver license', 'good 4 u', 'deja vu', 'traitor', 'happier than ever']
print(canciones)

#aplicar metodo append para agregar una cancion al final de la lista
lista_reproduccion = canciones.copy()
lista_reproduccion.append("teenage dream")

#aplicar insert para agregar una cancion en una posicion especifica de la lista (en la segunda posición;)
lista_reproduccion.insert(1, "can't catch me now")

print ("\n Lista despues de append e inset: ")
print(lista_reproduccion)

#------------------------------------------------------------------------------------
#aplicar extend() para fusionar con esta lista: 
# ["Bonus Track 1", "Bonus Track 2"].
#------------------------------------------------------------------------------------
bonus_tracks = ["Bonus Track 1", "Bonus Track 2"]
lista_reproduccion.extend(bonus_tracks)
print ("\n Lista despues extend: ")
print(lista_reproduccion)

#------------------------------------------------------------------------------------
#Usa remove() para eliminar una canción por su nombre y pop() para eliminar la última canción, guardando el valor eliminado e imprimiéndolo.
#------------------------------------------------------------------------------------
ultima_cancion = lista_reproduccion.pop() #elimina la ultima cancion y la guarda en la variable ultima_cancion
print(f"\n La ultima cancion eliminada es: {ultima_cancion}")


lista_reproduccion.remove("deja vu") #elimina la cancion "deja vu" de la lista
print(f"\n Lista despues de remove y pop: {lista_reproduccion}")

#------------------------------------------------------------------------------------
#Usa sort() para ordenar la lista alfabéticamente y muéstrala ordenada.
#------------------------------------------------------------------------------------
lista_reproduccion.sort

print("\n ✅ LISTA ORDENADA : ")
print(lista_reproduccion)

#------------------------------------------------------------------------------------
print("="*75)
print(" ----🥁RESPUESTAS---- usando metodos ")
print("="*75)

print("¿Cuántas canciones tiene la playlist🎤🤔?")
print(len(lista_reproduccion))

print("¿En qué posición está la primera canción que agregaste?🤔")
print(lista_reproduccion.index ("teenage dream"))

print("¿Cuántas veces aparece el string 'Bonus Track 1'?🤔")
print(lista_reproduccion.count("Bonus Track 1"))
print("="*75)