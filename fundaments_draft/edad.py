print("=" *69)
print("Este es el ejercicio 10 - PROGRAMA PARA DETERMINAR EDAD - CATEGORIAS 📐")

# Solicitamos la edad al usuario y la convertimos a entero
edad = int(input("Ingrese su edad para determinar su categoría: "))

# Evaluamos los rangos de menor a mayor
if edad < 0:
    print("Error: La edad no puede ser un número negativo.")
elif edad <= 5:
    print("Categoría: Infante")
elif edad <= 10:
    print("Categoría: Niño")
elif edad <= 15:
    print("Categoría: Pre adolescente")
elif edad <= 18:
    print("Categoría: Adolescente")
elif edad <= 25:
    print("Categoría: Pre adulto")
elif edad <= 40:
    print("Categoría: Adulto")
elif edad <= 55:
    print("Categoría: Pre anciano")
else:
    # Si no cumplió ninguna de las anteriores, automáticamente es 56 o mayor
    print("Categoría: Anciano")

print("=" *69 )