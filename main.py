import Calculs as calc

sep = "--------------------"

c = calc.Calculs()                                  

A = []
B = []
col = {}

print(sep)
typ = input("Régression ou Classification [R / C] : ").upper()
dim = int(input("\nDimension [1 - 26] : "))
for i in range(int(dim)):
    A.append(int(input("X : ")))
    B.append(int(input("Y : ")))

if dim == 1:
    c.Manhattan(A, B, col)
elif dim == 2:
    c.Euclidienne(A, B, col)
else:
    c.Chebyshev(A, B, col)

print(col)
c.tri(col)
print(col)
c.toGraphe(col)

for val in col:
    print(val, ": ", col[val])
if typ == 'R':
    print("\nMoyenne :", c.regression(col, dim))
else:
    print("\nPlus courant :", c.classification(col, dim))
    