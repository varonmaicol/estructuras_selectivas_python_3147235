'''
actividad_1 
en un sistema de automatizacion 
industrial un motor puede estar encendido o apagado 
si la tempetratura de la maquina supera los 80° el 
motor debe apagarse automaticamente. Escribe un 
programa que controle el estado del motor y lo apague 
si la temperatura supera los 80°
'''
#Ejercicio 
tem = int(input("Ingrese la temperatura del motor: "))
if tem <= 80:
    print ("El motor esta en funcionamiento")
    print ("puede seguir trabajando")
else:
    print("El motor se apagara automaticamente")
    print("no puede seguir trabajando por alta temperatura")
print("fin programa")