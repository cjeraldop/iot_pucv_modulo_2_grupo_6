#Escriba un programa que considere la siguiente tabla para mostrar el total de impuestos a pagar por una persona según su sueldo

print("Cálculo de impuestos según sueldo")
sueldo = float(input("Ingrese el sueldo: "))

impuestos=0;

if sueldo < 1000: impuestos = 0;
elif sueldo >= 1000 and sueldo < 2000: impuestos = sueldo*0.05;
elif sueldo >= 2000 and sueldo < 4000: impuestos = sueldo*0.10;
else: impuestos = sueldo*0.12;

print ("Usted pagará", round(impuestos,3), "de impuesto")