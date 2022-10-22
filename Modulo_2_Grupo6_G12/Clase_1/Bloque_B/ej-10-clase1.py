#Programa para simular pago de impuestos según sueldo
sueldo = int(input('Ingrese su sueldo: '))

#condiciones
if sueldo < 1000:
    print('Usted pagará 0 de impuestos')
elif sueldo < 2000:
    imp = sueldo*0.05
    print('Usted pagará: ', imp, 'por concepto de impuestos')
elif sueldo < 4000:
    imp = sueldo*0.1
    print('Usted pagará: ', imp, 'por concepto de impuestos')
else:
    imp = sueldo*0.12
    print('Usted pagará: ', imp, 'por concepto de impuestos')