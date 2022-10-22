'''
Cree una función codigo_hora(codigo) que reciba un código cifrado de sólo números y el caracter ‘:’ y entregue el código descrifrado. La regla de descifrado es la siguiente: sumar cada dígito anterior al caracter ‘:’ y calcular el resto de la división entera entre esa suma y 24. Luego, lo mismo con los dígitos después del carácter ‘:’, pero ahora el resto de la división es entre esa suma y 60.

>>> codigo_hora(‘776199:68556’)
‘15:30’
'''

def codigo_hora (codigo):
    palabra = codigo.split(sep=":")
    palabra1=list(palabra[0])
    palabra2=list(palabra[-1])
    i=0
    j=0
    sum1=0
    sum2=0
    while i<len(palabra1):
        sum1=(int(palabra1[i])+sum1)
        i+=1
    div1=int(sum1%24)
    while j<len(palabra2):
        sum2=(int(palabra2[j])+sum2)
        j+=1
    div2=int(sum2%60)

    return (str(div1)+":"+str(div2))

codigo= str(input("ingrese hora codificada :"))
print (codigo_hora(codigo))