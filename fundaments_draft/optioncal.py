#crear una calculadora- en este archivo me voy aretar y tratar de buscar y seguir varias formas de dar solucion a este ejercicio.
#ejercicio de calculadora basica- el programa debe solicitar al usuario dos numeros y la operacion que desea realizar, luego mostrar el resultado de la operacion.

print("Bienvenido a la calculadora basica")
print("1= Suma")
print("2= Resta")
print("3= Multiplicación")
print("4= División")
option = int (input("Ingrese la operación que desea realizar: "))

if (option in [1, 2, 3, 4]):
    print("Ingrese el primer número: ")
    num1 = float (input())
    print("Ingrese el segundo número: ")
    num2 = float (input())

#UNA OPCION ERA TAMBIEN : num1= int(input("Ingrese el primer numero")) y num2= int(input("Ingrese el segundo numero"))- PERO EN ESTE CASO SOLO SE PODRAN REALIZAR OPERACIONES CON NUMEROS ENTEROS, SI SE DESEA REALIZAR OPERACIONES CON NUMEROS DECIMALES, SE DEBE UTILIZAR LA FUNCION float() PARA CONVERTIR LOS NUMEROS INGRESADOS A DECIMALES.

    if option == 1: #== ES UN OPERADOR DE COMPARACION, SE UTILIZA PARA COMPARAR DOS VALORES, SI LOS VALORES SON IGUALES, LA EXPRESION DEVUELVE TRUE, SI LOS VALORES SON DIFERENTES, LA EXPRESION DEVUELVE FALSE. EN ESTE CASO, SE COMPARA LA VARIABLE option CON EL VALOR 1, SI option ES IGUAL A 1, LA EXPRESION DEVUELVE TRUE Y SE EJECUTA EL BLOQUE DE CODIGO DENTRO DEL IF, SI option ES DIFERENTE A 1, LA EXPRESION DEVUELVE FALSE Y SE PASA AL SIGUIENTE IF.
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
#EN ESTE CASO, SE UTILIZA LA FUNCION f-STRING PARA MOSTRAR EL RESULTADO DE LA OPERACION, PERO TAMBIEN SE PODRIA UTILIZAR LA FUNCION print() CON CONCATENACION DE STRINGS, COMO POR EJEMPLO: print("El resultado de la suma es: " + str(resultado)) - PERO EN ESTE CASO SE DEBE CONVERTIR EL RESULTADO A STRING PARA PODER CONCATENARLO CON EL STRING "El resultado de la suma es: ", POR ESO ES MAS FACIL UTILIZAR LA FUNCION f-STRING PARA MOSTRAR EL RESULTADO DE LA OPERACION.  

    elif option == 2:
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    
    elif option == 3:
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    
    elif option == 4:
        if num2 != 0:
            resultado = num1 / num2 #EN ESTE CASO, SE UTILIZA EL OPERADOR DE DIVISION / PARA REALIZAR LA DIVISION ENTRE num1 Y num2, PERO ANTES DE REALIZAR LA DIVISION, SE VERIFICA SI num2 ES DIFERENTE A 0, YA QUE SI num2 ES 0, LA DIVISION NO SE PUEDE REALIZAR Y SE MUESTRA UN MENSAJE DE ERROR. SI num2 ES DIFERENTE A 0, SE REALIZA LA DIVISION Y SE MUESTRA EL RESULTADO.
            
#en caso de que este fuera entero y se quisiera mostrar un resultado entero, se podria utilizar el operador de division entera // en lugar del operador de division /, PERO EN ESTE CASO SE DEBE TENER EN CUENTA QUE SI num1 O num2 SON DECIMALES, EL RESULTADO DE LA DIVISION ENTERA SERÁ UN ENTERO, POR LO QUE SE DEBE UTILIZAR EL OPERADOR DE DIVISION / PARA OBTENER UN RESULTADO DECIMAL SI num1 O num2 SON DECIMALES.
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")

else :
    print("Opción no válida. Por favor, ingrese una opción entre 1 y 4.")