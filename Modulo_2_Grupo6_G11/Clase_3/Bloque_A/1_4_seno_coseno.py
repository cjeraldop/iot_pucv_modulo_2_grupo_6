'''
Las funciones seno y coseno, pueden ser representadas por sumas infinitas:

1) Escriba la función factorial_reciproco(n), que retorne el valor de 1/n!
2) Escriba la función signo(n) que retorne 1 cuando n es par, y -1 cuando n
es impar.
3) Escriba las funciones seno_aprox(x, m) y coseno_aprox(x, m) que
aproximen el seno y el coseno de x, usando los primeros m términos de las
sumatorias.
'''

def factorial_reciproco(n):
    i=1
    prod = 1
    while i <= n:
        prod *=i # prod = prod*i
        i += 1
    return 1/prod
  
def signo(n):
    if n%2==0:
        return 1
    return -1

def seno_aprox(x, m):
  termino = 0
  valor_aproximado = 0
  while termino < m:
    valor_aproximado += signo(termino) * x ** (2 * termino + 1) * factorial_reciproco(2 * termino + 1)
    termino+=1
  return round(valor_aproximado,3)

def coseno_aprox(x, m):
  termino = 0
  valor_aproximado = 0
  while termino < m:
    valor_aproximado += signo(termino) * x ** (2 * termino) * factorial_reciproco(2 * termino)
    termino+=1
  return round(valor_aproximado,3)

x = 180
m = 10
print("Aprox Seno:" , seno_aprox(x,m))
print("Aprox Coseno: ", coseno_aprox(x,m))