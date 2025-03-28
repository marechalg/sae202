import Calculs as calc

sep = "--------------------"

c = calc.Calculs()                                  

A = []
B = []
col = {}

print(sep)
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

col = c.tri(col)
c.toGraphe(col)

typ = input("Régression ou Classification [R / C] : ").upper()
for val in col:
    print(val, ": ", col[val])
if typ == 'R':
    print("\nMoyenne :", c.regression(col, dim))
else:
    print("\nPlus courant :", c.classification(col, dim))


c.kMeans(col)
    