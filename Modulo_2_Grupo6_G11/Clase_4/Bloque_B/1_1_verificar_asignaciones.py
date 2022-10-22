'''
Considere las siguientes asignaciones:

>>> a = (2, 10, 1991)
>>> b = (25, 12, 1990)
>>> c = (‘Donald’, True, b)
>>> x, y = ((27, 3), 9)
>>> z, w = x
>>> v = (x, a)

Si usar el computador, indiquen en grupo cuál es el resultado y el tipo de las siguientes expresiones. Luego,
verifique en el computador.

1. a < b 7. a + b[1:5]
2. y + w 8. (a + b)[1:5]
3. x + a 9. str(a[2]) + str(b[2])
4. len(v) 10. str(a[2] + b[2])
5. v[1][1] 11. str((a + b)[2])
6. c[0] 12. str(a + b)[2][0]
'''

a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

print("1. a < b -->", a < b,  "     7. a + b[1:5] -->", a + b[1:5])
print("2. y + w -->", y + w, "      8. (a + b)[1:5] -->", (a + b)[1:5])
print("3. x + a -->", x + a,  "     9. str(a[2]) + str(b[2]) -->", str(a[2]) + str(b[2]))
print("4. len(v) -->", len(v), "   10. str(a[2] + b[2]) -->", str(a[2] + b[2]))
print("5. v[1][1] -->", v[1][1], " 11. str((a + b)[2]) -->", str((a + b)[2]))
print("6. c[0] -->", c[0] ,"       12. str(a + b)[2][0] -->", str(a + b)[2][0])