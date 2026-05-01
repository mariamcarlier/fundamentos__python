print('hello word!')

print('yo soy mariam')
#usar reglas 
AprendizSena = "mariam carlier"
print(AprendizSena)
snake_case = " el snake case con guion bajo- en variables se usa mas en las empresas" #se utiliza mas en las empresas 
print(snake_case)
camelCase = "EL CAMELCASE SE asocia con un camello" #seutiliza en muchos programas
print(camelCase)
PascalCase= "sena" #
print(PascalCase)

nombre = "mariam "
edad = 18
altura = 1.59
activo =  True
correo = "mariam00estudio@gmail.com"
telefono = "3003600203"
cedula = 1057980448

print(type(nombre), nombre)     #string
print(type(edad), edad)         #integer
print(type(altura), altura)     #float
print(type(activo), activo)     #boolean
print(type(cedula), cedula)     #integer
print(type(correo), correo)     #string
print(type(telefono), telefono) #string
print(type(cedula), cedula)

año_de_nacimiento = "2007"
año_de_nacimiento = int(año_de_nacimiento) #convertir string a entero   

print(año_de_nacimiento)

#convertir las variables pára ver su comportamiento
edad_float = float(edad)
print((type)(edad_float), edad_float) #float

altura_string = str(altura) #convertir float a string
print((type)(altura_string), altura_string) #string

altura_int = int(altura) #convertir float a entero
print((type)(altura_int), altura_int) #integer

cedula_string = str(cedula)#estaba en entero y la convierto en string

"""
    este es un comentario de varias lineas, se utiliza para explicar el codigo o para escribir notas, no afecta el funcionamiento del programa
"""
#IDENTACION EN PYTHON - es la forma en que se organizan las lineas de codigo, se utiliza para indicar que un bloque de codigo pertenece a una estructura de control, como un if, for, while, etc. en python se utiliza la indentacion con espacios o tabuladores, pero se recomienda utilizar espacios para evitar errores de indentacion. la indentacion es muy importante en python, ya que si no se utiliza correctamente, el programa no funcionara correctamente.
if 5>3:
    print("5 es mayor que 3") #este bloque de codigo pertenece al if, por eso esta indentado


#INPUTS - es una funcion que permite al usuario ingresar datos por teclado, el valor ingresado se almacena en una variable, el valor ingresado siempre es un string, por lo que si se desea utilizar como otro tipo de dato, se debe convertir utilizando las funciones de conversion, como int(), float(), etc.
nombre_usuario = input("Ingrese su nombre: ") #el valor ingresado se almacena en la variable nombre_usuario
print("Hola, " + nombre_usuario) #se concatena el string "Hola, "

edad = input("Ingrese su edad: ")
edad = int(edad) 
"""
convertir el string a entero- aqui utilize la funcion de conversion int() para convertir el string ingresado por el usuario a un entero, ya que la edad es un numero entero y no se puede realizar operaciones matematicas con un string.
"""

#La función print() permite incluir variables o expresiones como argumento, lo que nos permite combinar texto y variables:
print(type(edad), edad) 

print(f"Hola, {nombre_usuario}. Tu edad es {edad} años.") 
#f-string es una forma de formatear cadenas de texto, permite incluir variables dentro de la cadena utilizando llaves {}. Es una forma mas legible y facil de escribir que la concatenacion tradicional.

print("bienvenido"+ nombre_usuario + " , tienes " + str(edad) + "años .")#la basica es esta: 