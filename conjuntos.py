# CONJUNTOS (SETS) en Python

# Estructura de un conjunto

conjunto= set()
print(type(conjunto)) # <class 'set'>

# ----- CREACION -----
lenguajes = {"Python", "Java" , "C++" , "Python ", "Java"}
print (lenguajes) #quito la duplicidad- y sin orden fijo

# ¡IMPORTANTE : conjunto vacio vs diccionario vacio¡
conjunto_vacio =set()
diccionario_vacio = {} # NO es un set

#los conjuntos no se pueden modificar
#---  Metodos de modificacion  ---
frutas= {"mango", "guayaba", "mora"}
frutas.add("maracuya")      #Agrega un elemento
frutas.add("mango")         #NO HACE NADA, YA EXISTE

frutas.remove("mora")       #Elimina; lanza KeyError si no existe
frutas.discard("papaya")    #Elimina; NO lanza KeyError si no existe

elem = frutas.pop()         #ELIMINA Y RETORNA UN ELEMENTO ALEATORIO
print(frutas)

# =================VERIFICAR PERTINENCIA : 0 (1)=========================
print("Python" in lenguajes) #true - instantaneo sin importar el tamaño
print("COBOL" in lenguajes)  #false

print("=" *69)
python_devs = {"Ana", "Luis", "Marta", "Carlos" , "Sofia"}
java_devs = {"Luis", "Carlos", "Pedro", "Laura"}
# DEV QUE SABEN PYTHON Y JAVA
print("Operaciones de Teoría de Conjuntos",
       "\n devs que saben python y java")
print(python_devs)
print(java_devs)
print("=" *69)

print(" UNION DE CONJUNTOS (|) - todos los elementos de ambos conjuntos")
print("=" *69)
todos = python_devs | java_devs
# O tambien : python_devs.union(java_devs)
print("Union:" , todos) 
# - no hace duplicados ( luis y carlos que saben los dos )
#Union: {'Carlos', 'Sofia', 'Luis', 'Pedro', 'Laura', 'Ana', 'Marta'}

# --------------------------------------------------------------------------
print("=" *69)
print(" INTERSECCION (&) : Solo los que estan en ambos")
print("=" *69)
# --------------------------------------------------------------------------
ambos = python_devs & java_devs
# O tambien : python_devs.union(java_devs)
print("Intersección:" , ambos) # Intersección: {'Luis', 'Carlos'}


# --------------------------------------------------------------------------
print("=" *69)
print(" DIFERENCIA (-) : Los de A que NO ESTÁN en B")
print("=" *69)
# --------------------------------------------------------------------------
solo_python = python_devs - java_devs
print("Sólo Python:" , solo_python) # Sólo Python: {'Ana', 'Sofia', 'Marta'}

solo_java = java_devs - python_devs
print("Solo Java:" , solo_java) # {'Laura', 'Pedro'}

# --------------------------------------------------------------------------
print("=" *69)
print(" DIFERENCIA SIMÉTRICA ")
print("=" *69)
# --------------------------------------------------------------------------