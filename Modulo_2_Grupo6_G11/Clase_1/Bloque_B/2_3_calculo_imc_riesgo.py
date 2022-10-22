#Escribaunprogramaquerecibacomoentradalaestatura,elpesoylaedaddeunapersona,yelentreguelacondiciónderiesgo.ConsiderequeelIMCsecalculacomo:peso/estatura**2

print ("Obtener la condición de riesgo basado en el IMC de la persona")
edad = int(input("Ingrese la edad: "))
estatura = float(input("Ingrese la estatura en metros: "))
peso = float(input("Ingrese la el peso en kilogramo: "))

imc = peso / (estatura**2)
nivel_de_riesgo = ''

if edad <45:
  nivel_de_riesgo = "Bajo" if imc < 22 else "Medio"
else:
  nivel_de_riesgo = "Medio" if imc < 22 else "Alto"

print ("La condición de riesgo calculada es:",nivel_de_riesgo)