# Diccionarios (Caracteristicas a un Elemento)

# Creacion de un diccionario

# Estructura  de un diccionario
    # "llaves/KEYS" : "VALORES"
diccionario = {
    "clave_1" : "valor_1",
    "clave_2" : "valor_2",
    "clave_3" : "valor_3",
}

# CREAR UN DICCIONARIO VACIO:
diccionario_vacio = {}

# 
diccionario_aprendiz = {
    "nombre" : "Emily",
    "apellido" : "Smith",
    "programa" : "ADSO",
    "ficha" : 3321349 ,
    "edad" : 22
    }

print(type(diccionario_aprendiz)) # <class 'dict'>
print(diccionario_aprendiz) # {'nombre': 'Emily', 'apellido': 'Smith', 'programa': 'ADSO', 'edad': 22}

# Obtener un valor de un diccionario
print(diccionario_aprendiz["programa"]) #ADSO
print(diccionario_aprendiz.get("programa")) #ADSO

# Obtener solo las claves de un diccionario
print(diccionario_aprendiz.keys()) # dict_keys(['nombre', 'apellido', 'programa', 'ficha', 'edad']) 

# Obtener solo los valores de un diccionario
print(diccionario_aprendiz.values()) # dict_values(['Emily', 'Smith', 'ADSO', 3321349, 22])

# Obtener clave y valor
print(diccionario_aprendiz.items())

# Agregar un nuevo elemento al diccionario
diccionario_aprendiz["correo"] = "siahysinokm@gmail.com"

# Modificar un valor de un diccionario
diccionario_aprendiz["programa"] = "Multimedia"
print(diccionario_aprendiz)

 # METODO UPDATE
diccionario_aprendiz.update({"nombre":"Estrella"}) #modifica un elemento
diccionario_aprendiz.update({"cuidad": "Duitama"}) #agrega un nuevo elemento
print(diccionario_aprendiz)

#--------------   IN  -------------------------
#🧐se guarda temporalmente el valor de la clave "programa" para luego modificarlo
#🧐se ponen nombres de variables descriptivas

#Comprobar pertinencia
if "ficha" in diccionario_aprendiz:
    print("ficha es una de las propiedades de este producto")

#RECORRER UN DICCIONARIO CON UN CICLO FOR (no es un ciclo infinito)
    # Recorrer solo las claves del diccionario      KEYS
for clave in diccionario_aprendiz.keys():
    print(clave)

    #Recorrer solo con los valores del diccionario  VALUES
for valor in diccionario_aprendiz.values():
    print(valor)

    #Recorrer con clave y valor del diccionario     ITEMS
for clave, valor in diccionario_aprendiz.items():
    print(f"la clave es: {clave} y el valor es: {valor}")

#  Eliminar elementos en un diccionario POP
diccionario_aprendiz.popitem()# elimina el ultimo elemento agregado / duitama
print(diccionario_aprendiz)

diccionario_aprendiz.pop("edad") #elimina un elemento especifico / edad 
print(diccionario_aprendiz)

#ELIMINAR TODOS LOS ELEMNENTO DEL DICCIONARIO
diccionario_aprendiz.clear()
print(diccionario_aprendiz) # {}

# ===================================
# DICCIONARIOS ANINADOS
# ==================================
#diccionario general y diccionarios individuales con valor

aprendices = {
    "aprendiz_1" : {
        "nombre": "Melquisedec",
        "apellido": "Alvarez",
        "programa": "SST",
        "ficha": "33245647",
        "edad": 35
    },
    "aprendiz_2" : {
        "nombre": "Felipe",
        "apellido": "Sandoval",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 32
    },
    "aprendiz_3" : {
        "nombre": "Sara",
        "apellido": "Castro",
        "programa": "Topografia",
        "ficha": "3321678",
        "edad": 17
    },
}

#Acceder a un valor en un diccionario aninado
print(aprendices["aprendiz_2"]["programa"]) #ADSO

#Recorrer un diccionario anidado con un ciclo for
for aprendiz, datos in aprendices.items():
    print(f"{aprendices}: ")
    for clave, valor in datos.item():
        print(f" {clave}: {valor}")