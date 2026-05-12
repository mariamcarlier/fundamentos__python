#Actividad 1: Inventario de la Tienda EscolaR

productos = ['Cuadernos', 'Lápices', 'Borradores', 'Colores', 'Libros', 'Carpetas']
precios = [ 8500, 2000 , 1500 , 27000 , 60000 , 6500]
cantidades = [150 , 100 , 87 , 23 , 55 , 30]

#Imprime las tres listas completas y luego usa len() para mostrar cuántos productos tiene el inventario.
cantidad_productos = len(productos)
print("="*75)
print ("-- inventario de la tienda escolar🏫🎒 --"
       "\n Productos:  " , productos,
       "\n Precios:    " , precios,
       "\n Cantidades: " , cantidades,
       "\n Cantidad de productos: " , cantidad_productos,)
print("="*75)

#se asocia cada producto (no es tan optimo pero es una forma de hacerlo)
print(f"El producto {productos[0]} tiene un precio de {precios[0]} y una cantidad de {cantidades[0]} unidades.")
print(f"El producto {productos[1]} tiene un precio de {precios[1]} y una cantidad de {cantidades[1]} unidades.")
print(f"El producto {productos[2]} tiene un precio de {precios[2]} y una cantidad de {cantidades[2]} unidades.")
print(f"El producto {productos[3]} tiene un precio de {precios[3]} y una cantidad de {cantidades[3]} unidades.")
print(f"El producto {productos[4]} tiene un precio de {precios[4]} y una cantidad de {cantidades[4]} unidades.")
print(f"El producto {productos[5]} tiene un precio de {precios[5]} y una cantidad de {cantidades[5]} unidades.")

print("="*75)
#PUNTO 5 
print(type(productos)) #<class 'list'>
print(type(productos[0]))#<class 'str'>
#la diferencia de este tipo de dato se da porque a comparandolos, la primer linea ingresa la variable en su totalidad, estos son todos los productos, por ello nos da list - en cambio en la segunda linea se esta llamando a un producto en especifico, por ello la consola nos da string
