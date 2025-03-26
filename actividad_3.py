
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
=> Para el caso de presentacion de servicios 
  se debe solicitar 
  -el valor del contrato 
  -el numeros de meses del contrato
  - la antiguadad del empleado (años)
  El salario neto , en el caso se calcula:
  1- dividir el valor del contrato por numero de meses 
  2- restar el 15% de valor anterior, 
    por concepto de EPS(SALUD)
  3- restar el 10% de salario mensual ,
   por concepto de Pension
  4- si el empleado tiene una antiguedad 
  superior o igual a 10 años 
  tiene una bonificacion del 0.5% 
  sobre el salario mensual 
=> para el caso de contrato a termnino indefinido 
  se debe solicitar 
  - Aantiguedad  (año)
  -Grado o escalafon (1-5)
  - el salario minimo
  El salario neto se calcula de acuerdo 
  a la siguiente tabla:
  - grado 1: 1.5  SM
  - grado 2: 1.7 SM
  - grado 3: 2.0 SM
  - grado 4: 2.5 SM
  - grado 5: 3.0 SM
  la bonificacion estara acorde a 
  Los siguientes rangos segun la 
  Antiguedad 
  - entre 1 y 5 años :1 %del salario mensual 
  - entre 6 y 10 años : 2 % el salario mensual 
  - mayot de 10 años : 3 % el salario mensual 
  para este caso, los descuentos de ley son :
  - 25% por concepto de EPS
  - 22% por concepto de pension
  - 0.1% por concepto de ARL
'''
contrato = input("ingrese tipo de contrato es ")
# inicializar variables: 
# dar valor inicial a un variable 
# asi no utilice en el momento
salario_neto = 0 
if contrato == "a":
 print("Eligio: contrato a termino indefinido")
 if contrato == "a":
    print ("Eligio: contrato a termino indefinido")
    antiguedad = int(input("Ingrese la antiguedad del empleado (Año):"))
    grado = int(input("Ingrese el grado del empleado:(1-5)"))
    salario_neto= int(input("Ingrese el salario neto del empleado:"))
    salario_minimo = int(input("Ingrese el salario minimo:"))
    if grado == 1:
        salario_neto = salario_minimo*1.5
    elif grado == 2:
        salario_neto = salario_minimo*1.7
    elif grado == 3:
        salario_neto = salario_minimo*2.0
    elif grado == 4:
        salario_neto = salario_minimo*2.5
    elif grado == 5:
        salario_neto = salario_minimo*3.0
    if antiguedad >= 1 and antiguedad <= 5:
        salario_neto = salario_neto + (salario_minimo*0.01)
    elif antiguedad >= 6 and antiguedad <= 10:
        salario_neto = salario_neto + (salario_minimo*0.02)
    elif antiguedad >= 10:
        salario_neto = salario_neto + (salario_minimo*0.03)
    salario_neto = salario_neto - (salario_neto*0.25) - (salario_neto*0.22) - (salario_neto*0.001)
elif contrato == "b":
 print("Eligio: contrato por presentacion de servicios")
 valor_contrato = int(input ("Ingrese el valor del contrato:   "))
 numero_meses = int(input ("Ingrese el numero de meses trabajados:  "))
 antiguedad  = int(input ("Ingrese la antiguedad delempleado en años:   "))
 salario_mensual = valor_contrato / numero_meses
 EPS = salario_mensual * 0.15 
 pension = salario_mensual *0.10 
 bonificacion = salario_mensual * 0.05 
 salario_neto = salario_mensual - EPS - pension 
if antiguedad >= 10: 
 salario_neto = salario_mensual + bonificacion
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
