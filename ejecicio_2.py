'''
un universidad ofrece un descuento a los estudiantes que depende 
del estrato y la edad. Si el estrato es 1 y su edad es menor a 18
el descuento sera de 20% sobre el valor de la matrucula.Si el estrato es 
1 y el estudiante tiene 18 o mas , el descuento de 10% y si el estrato es 
2 y la edad es 18 o mas, el descuento sera del 5%. 
''' 

estrato = int(input("Ingrese el estrato (1 o 2): "))
edad = int(input("Ingrese la edad del estudiante: "))
matricula = input("Ingrese el valor de la matrícula: ")

if estrato == 1:
    if edad < 18:
        descuento = 0.02
        descuento = 0.01  
elif estrato == 2 and edad >= 18:
    descuento = 0.05  
else:
    descuento = 0.00  

monto_descuento = matricula * descuento

matricula_final = matricula - monto_descuento

print("El descuento es del {descuento * 100}%")
print("El monto del descuento es: {monto_descuento}")
print("El valor final de la matrícula es: {matricula_final}")
print("fin del programa")