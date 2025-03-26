'''
if anidados :
if dentro de otros if 
Syntax:
if condicion 1:
  if condicion 2: 
     print("mensaje")
     if condicion 3: 
         print("mensaje")
     if condicion 4: 
     print("mensaje")
 if condicion 5: 
     print("mensaje")
   else:
     print("mensaje")
no confundir el elif (if en casada)
'''
#EJEMPLO 1
#Modifique el ejercicio del la edad 
#para las siguientes condiciones 
#1. si es mayor de 18 años,
#  pero no tiene documento, no ouede votar 
# de lo contrario si puede votar 
#2 si es menor de 18 años 
# no puede votar  
# utilice la estructura de is anidados
edad = int(input("ingrse la edad: "))
if edad >= 18 : 
    documento = input("Tiene documento? (SI/NO): ")
    if documento == "si": 
        print("puede votar")
    else :
        print ("No puede votar")
else :
    print ("No puede votar")