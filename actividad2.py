# Actividad 2: Calculadora de Notas
# 1. Solicitar las tres calificaciones parciales
print("--- Calculadora de Promedio de Notas ---")

# Aplicamos anotación de tipo (float) para mayor claridad
nota1: float = float(input("Ingrese la primera nota parcial: "))
nota2: float = float(input("Ingrese la segunda nota parcial: "))
nota3: float = float(input("Ingrese la tercera nota parcial: "))

# 2. Calcular el promedio de las tres notas
# Sumamos las notas y dividimos por la cantidad (3)
promedio_real = (nota1 + nota2 + nota3) / 3

# 5. Investigando round(): Redondeamos a dos decimales
# Sintaxis: round(numero, cantidad_decimales)
promedio = round(promedio_real, 2)

# 3. Calcular cuántos puntos faltan para la nota máxima (5.0)
puntos_faltantes = round(5.0 - promedio, 2)

# 4. Determinar si el estudiante aprueba (promedio >= 3.0)
# Esto devuelve un valor Booleano (True o False)
aprobado = promedio >= 3.0

# 5. Mostrar todos los resultados con formato legible (f-strings)
print("\n" + "="*30)
print("      RESULTADOS FINALES      ")
print("="*30)
print(f"Notas ingresadas: {nota1}, {nota2}, {nota3}")
print(f"Promedio final:   {promedio}")
print(f"Puntos para el 5.0: {puntos_faltantes}")

# Usamos un pequeño condicional para que el mensaje sea más amable
if aprobado:
    print(f"Estado: ¡APROBADO! ✅ con un promedio de {promedio}")
else:
    print(f"Estado: REPROBADO ❌ con un promedio de {promedio}")
print("="*30)
