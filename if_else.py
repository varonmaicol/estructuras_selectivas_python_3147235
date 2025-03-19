'''
if_else 
determinar lo tipos de caminos 
de ejecucion basados en la  
evaluacion de una condicional 
sintaxis 
if condicional : 
 instruccion1 
 instruccion2 
else :
 instruccion3
 instruccion4  
'''
#ejemplo 
#elabore un programa de python 
# que determine si  una persona es mayor o menor de edad 
# y por tanto, habilitada para 
#votar 
edad = input (input("ingrese la edad"))
documento = False
if edad >= 18 and documento==True:
    print ("usted es mayor de edad ")
    print("puede votar gansgter")
else : 
    print("usted es menor de edad")
    print("O")
    print("no puede votar bro")
print ("fin del programa")