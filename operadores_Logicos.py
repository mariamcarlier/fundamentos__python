# OPERADORES LOGICOS 
#INPUT AND OUTPUT 

# 1. A and B
# en resumen si las dos se cumplen y solo es V = TRUE = V 

print (True and True) # Si ambos son verdaderos
print (True and False) # Si hay verdadero y falso , no se cumple
print (False and True)
print (False and False) # = FALSE 

# 2. A or B
# en resumen hay mas flexibiblidad - se cumple cuando al menos una de cumple
print(True or True) # = TRUE
print(True or False) # = TRUE
print(False or True) # = TRUE
print(False or False) # solo no se cumple cuando las dos no se cumplen = false

# 3. A not B 
print (not False) # Si es verdadero = False
print (not True)  # Si es falso = True 

#EJERCICIOS 
# 1 AND
print ("EJERCICIO DE AND CON VALORES")
print (5 > 3 and 2 < 4) # = True
print (5 > 3 and 2 > 4) # = False

#2 OR
print("EJERCICIO DE OR")
print (3==3 or 2<4) #True
print (2<=2 or 3!=3) #true
print(2!=2 or 5<10) #true
print(10<5 or 5==6) #false

#3 NOT 
print("EJERCICIO DE NOT")