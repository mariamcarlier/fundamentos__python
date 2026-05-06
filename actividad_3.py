#EJERCICIO 3 - ACTIVIDAD CLASIFICADOR DE IMC
#PUNTO 1: Calcula el Índice de Masa Corporal con la fórmula: 
# IMC = peso / (estatura ** 2).
print("=" * 45)
print("--  CALCULADORA DE INDICE DE MASA CORPORAL (IMC)  --")
formula_imc = "IMC = peso / (estatura ** 2)"
print("=" * 45)

peso = float(input("Ingrese su peso en kg (ej: 55):"))
estatura = float(input("Ingrese su estatura (ej: 1.60): "))
imc = peso / (estatura ** 2)

print("=" * 45)

#para que aparezcan 2 decimales 
resultado_imc = round(imc,2)
print(f"Tu IMC es: {resultado_imc}")

# -----------------------------------------
if peso <= 0 or estatura <= 0:
    print("Si el resultado sale de IMC sale 0.0 ingreso mal el peso o la estatura")
    if resultado_imc <= 0.0:
        print("🔒⛔Error: El peso y la estatura deben ser valores positivos. ")
    print("Por favor reinicia el programa e intenta de nuevo")

print("=" * 45)

#COMPOSICION CORPORAL
if resultado_imc >= 18.9 and resultado_imc <= 24.9: #peso normal
    print("Tu peso es normal 🟢🥳")  
elif resultado_imc <= 18.5: #peso inferior al normal
    print("Tu peso es inferior al normal 🟣⚠️🫥")
    if resultado_imc <= 0.0:
        print("🔒⛔Error: El peso debe ser un valor positivo. Si el resultado sale de IMC sale 0.0 ingreso mal el peso " )


elif resultado_imc >= 25 and resultado_imc <= 29.9: #sobrepeso
    print("Te encuentras en sobrepeso ⚠️🟡👁️")
elif resultado_imc >= 30 and resultado_imc >=34.9 : #obecidad
    print("Tu estado actual segun tu peso es Obesidad 🟠⚠️")
elif resultado_imc > 35  :
    print("Tu estado actual segun tu peso es Obesidad Extrema 🔴⚠️")


