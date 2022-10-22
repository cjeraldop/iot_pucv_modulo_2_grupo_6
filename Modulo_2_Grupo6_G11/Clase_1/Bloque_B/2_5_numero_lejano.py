#Escriba un programa que permita ingresar 5 números enteros y determine cuál de los cuatro números es el más lejano al primero

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))
num4 = int(input("Ingrese el cuarto número entero: "))
num5 = int(input("Ingrese el quinto y último número entero: "))

dif_con_num2 =  abs(num1 - num2)
dif_con_num3 = abs(num1 - num3)
dif_con_num4 = abs(num1 - num4)
dif_con_num5 = abs(num1 - num5)

mayor_diferencia = max([dif_con_num2, dif_con_num3, dif_con_num4, dif_con_num5])

el_numero_mas_lejano=num1
if dif_con_num2 == mayor_diferencia: el_numero_mas_lejano = num2
elif dif_con_num3 == mayor_diferencia: el_numero_mas_lejano = num3
elif dif_con_num4 == mayor_diferencia: el_numero_mas_lejano = num4
else: el_numero_mas_lejano = num5
  
print ("El número más lejano al primero es: ", el_numero_mas_lejano)