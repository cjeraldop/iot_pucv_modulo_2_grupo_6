
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

codigo= str(input("Ingrese la hora codificada :"))
print (codigo_hora(codigo))