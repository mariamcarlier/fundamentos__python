print("="*75)
print("Actividad 2: 👁️⏳Análisis de Temperaturas Semanales 🌞😎")
print("="*75)
# INDICE        0   1   2   3   4   5   6   7   8   9   10  11  12  13
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

cantidad_datos =(len(temperaturas)) #len= longuitud 21 registros
print(f"La lista de temperaturas tiene {cantidad_datos} elementos.")

# punto 2 - usando idexacion para imprimir distintos datos
print("SEGUNDA LISTA - idexacion de datos usando índices positivos y negativos.")
print(f"Temperatura del primer día: {temperaturas[0]}°C") 
#el primer dia
print(f"Temperatura del último día: {temperaturas[-1]}°C") 
# el ultimo dia , (-1) ya que es el ultimo dato ingresado 
print(f"Temperatura del día 7 (mitad): {temperaturas[6]}°C")
# el dia 7 es el dato que esta en la posicion 6, ya que se empieza a contar desde el 0
print(f"Temperatura del penúltimo día: {temperaturas[-2]}°C")


print("="*75)
# punto 3 -usando slicing (:) IDEXACION para imprimir distintos datos
print("Desarrollo Usando Slicing (:) - IDEXACION= [inicio:fin:paso]")
print("="*75)

#1 -los primeros 7 dias- Utilize (:#)= el numero despues de : muestra los datos del inicio HASTA el numero escrito
#su punto de partida inicia y termina Hasta el numero ingresado
print(f"Temperaturas de la primer semana / dias (1-7), : {temperaturas [:6]}")

#2 -la segunda semana - Utilize (#:)= el numero antes de : muestra los datos DESDE ese numero hasta el final.
# su punto de patida fue desde el dia 7
print(f"Temperaturas de la segunda semana / dias (7-14), : {temperaturas [7:]}")

#3 mostar las temperaturas de los dias pares 
temperaturas_pares = temperaturas[0::2] # se muestra desde el indice 0 hasta el final de la lista, pero solo los elementos que estan en los indices pares, en este caso '18', '19', '22', '17', '25', '18', '22'
print(f"Temperaturas en posiciones/dias pares: {temperaturas_pares}")


c_invertido = temperaturas [::-1] # se muestra la lista de temperaturas en orden inverso, el -1 indica que se recorra la lista de atras hacia adelante
print(f"Temperaturas en orden inverso: {c_invertido}")
print("="*75)

# punto 4 - Calcula e imprime la temperatura promedio de cada semana por separado usando sum() y len() aplicados a los slices.
print("Temperatura promedio de la primer semana / dias (1-7): ", sum(temperaturas[:6])/len(temperaturas[:6]))
print("Temperatura promedio de la segunda semana / dias (7-14): ", sum(temperaturas[7:])/len(temperaturas[7:]))

#Bonus: Determina cuál de las dos semanas tuvo mayor temperatura promedio y muestra el resultado con un mensaje descriptivo.
promedio_primera_semana = sum(temperaturas[:6])/len(temperaturas[:6])
promedio_segunda_semana = sum(temperaturas[7:])/len(temperaturas[7:])

if promedio_primera_semana > promedio_segunda_semana:
    print("La primera semana tuvo una temperatura promedio mayor.")
elif promedio_primera_semana < promedio_segunda_semana:
    print("La segunda semana tuvo una temperatura promedio mayor.")
else:
    print("Ambas semanas tuvieron la misma temperatura promedio.")

