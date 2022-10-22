def factorial_reciproco(n):
    i = 1
    producto = 1
    while i <= n:
        producto *= i
        i += 1
    return 1 / producto

def signo(n):
    if n % 2 == 0:
        return 1
    else:
        return -1

def seno_aprox(x, m):
    term = 0
    valor_aprox = 0
    while term < m:
        valor_aprox += signo(term) * x ** (2 * term + 1) * factorial_reciproco(2 * term + 1)
        term += 1
    return round(valor_aprox, 3)


def coseno_aprox(x, m):
    term = 0
    valor_aprox = 0
    while term < m:
        valor_aprox += signo(term) * x ** (2 * term) * factorial_reciproco(2 * term)
        term += 1
    return round(valor_aprox, 3)

x = 4
m = 5
print("Seno_Aprox:", seno_aprox(x, m))
print("Coseno_Aprox: ", coseno_aprox(x, m))
