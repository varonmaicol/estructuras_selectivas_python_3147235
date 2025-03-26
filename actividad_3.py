
'''
elabore un programa 
que permita calcula el salario 
neto de un empleado 
depues de descontar los descuentos 
por conseptos de 
salud, pension, arl 
a. contrato a termnino indefinido
b. contrato por prestacion de 
  de servicios 
c. contrato de aprendizaje 
d. contrato po Jornal (FREELANCE)
=> para el caso de Jonal :
- se debe solicitar numero de 
- horas trabajadas y el valor a pagar  por hora 
* el total del salario se calcula 
  de multiplicar el numero de horas 
  por el valor a pagar  por hora 
'''
contrato = input("ingrese tipo de contrato es ")
# inicializar variables: 
# dar valor inicial a un variable 
# asi no utilice en el momento
salario_neto = 0 
if contrato == "a":
 print("Eligio: contrato a termino indefinido")
elif contrato == "b":
 print("Eligio: contrato por presentacion de servicios")
elif contrato == "c":
 print("Eligio: contrato d¿de aprendizaje")
 salrio_minimo =  int(input ("Ingrese el valor de salario  minimo "))
 salario_neto = salrio_minimo - (salrio_minimo * 0.75 )
elif contrato == "d":
 print ("Eligio:contrato po Jornal ")
 numero_horas =  int(input ("Ingrese el numero de horas "))
 valor_horas = int(input("ingrese le valor por hora a pagar"))
 salario_neto = numero_horas * valor_horas
else :
  print("Tipo de contrato no existente")
print("el salario neto es: " , salario_neto)
print("Fin del programa")
