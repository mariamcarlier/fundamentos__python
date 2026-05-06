#TRABAJO INTERACTIVO-
#CON INPUT - OPERADORES DE ASIGNACION - ARITMETICOS - COMPARACION -SENTENCIAS: IF, ELIF, ELSE - PRINT() 
# si es posible- F-STRINGS - FUNCION ROUND() - OPERADOR TERNARIO

print("=" * 45)
print("---💎  Bienvenido a Joyeria Oro del Sol  💎---")
print("=" * 45)

#DATOS DEL CLIENTE
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}, vamos a crear tu anillo ideal ")

# SELECCION DE ANILLO
print("TIPOS DE ANILLO: ")
print("1. Personal - Oro 18 k")
print("2. Al detal ")
print("3. Al por mayor")

opcion = int(input("Elige la opcion (1-3): "))

#ASIGNACION DE PRECIO
if opcion ==1:
    tipo ="Oro 18 k"
    precio_base = 50000
elif opcion ==2:
    tipo ="Oro 18 k"
    precio_base = 80000   
elif opcion ==3:
    tipo ="Oro 18 k"
    precio_base = 90000 
else:
    print("Opcion invalida, se asignara personal por defecto")
    tipo ="Oro - Personalizado"
    precio_base = 50000

print("=" * 45)
#TALLA
talla= int(input("Ingresa la talla del anillo (ej: 6-7-8):"))
# ====== EXTRAS ======
print("\nExtras disponibles:")
print("1. Grabado (+50.000)")
print("2. Piedra preciosa (+150.000)")
print("3. Ninguno")

extra_opcion = int(input("Elige un extra (1-3): "))

extra_precio = 0
extra = "Ninguno"

if extra_opcion == 1:
    extra = "Grabado"
    extra_precio = 50000
elif extra_opcion == 2:
    extra = "Piedra preciosa"
    extra_precio = 150000
elif extra_opcion == 3:
    extra = "Ninguno"
else:
    print("Opción inválida, sin extras.")

print("=" * 45)

# ====== OCASIÓN ======
print("\n¿Para qué ocasión es el anillo?")
print("1. Compromiso")
print("2. Regalo")
print("3. Uso personal")

ocasion = int(input("Elige una opción (1-3): "))

descuento = 0

if ocasion == 1:
    print("💖 ¡Descuento especial por compromiso!")
    descuento = 0.10
elif ocasion == 2:
    print("🎁 Incluiremos un mensaje especial.")
elif ocasion == 3:
    print("👌 Excelente elección para ti.")
else:
    print("Opción no válida.")

print("=" * 45)
# ====== CÁLCULO TOTAL ======
total = precio_base + extra_precio
descuento_valor = total * descuento
total_final = total - descuento_valor
print("=" * 45)

# ====== RESUMEN ======
print("\n========== RESUMEN DE COMPRA ==========")
print(f"Cliente: {nombre}")
print(f"Tipo de anillo: {tipo}")
print(f"Talla: {talla}")
print(f"Extra: {extra}")
print(f"Precio base: ${precio_base}")
print(f"Extra: ${extra_precio}")
print(f"Descuento: ${descuento_valor}")
print(f"TOTAL A PAGAR: ${total_final}")
print("======================================")

print("\n🙏 Gracias por confiar en nosotros.🤗")