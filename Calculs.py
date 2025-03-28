from math import *
from matplotlib import pylab as plt
import numpy as np
<<<<<<< HEAD
import random
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.cluster import KMeans
=======
<<<<<<< HEAD
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
=======
<<<<<<< HEAD
import random
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.cluster import KMeans
=======
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
>>>>>>> ccd39948d1adb57f1c950abcc32ac34ba8608cf0
>>>>>>> 12490a65a3db1f486fc6a83c106e6e180b570fb3
>>>>>>> 4b9a9240cce5531a6e19ee4a3b7d0d05bbd0931c

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Calculs(object):
    def Minkowski(self, A, B, p = 3):
        res = 0
        for i in range(len(A)):
            res += (abs(A[i] - B[i]) ** p)
        return res ** (1 / p)

    def Manhattan(self, A, B, col = {}):
        res = 0
        for i in range(len(A)):
            calc = abs(A[i] - B[i])
            col[i + 1] = calc
            res += calc
        return res
    
    def Euclidienne(self, A, B, col = {}):
        res = 0
        for i in range(len(A)):
            calc = (A[i] - B[i]) ** 2
            col[i + 1] = calc
            res += calc
        return sqrt(res)
          
    def Chebyshev(self, A, B, col = {}):
        max = 0
        for i in range(len(A)):
            calc = abs(A[i] - B[i])
            col[i + 1] = calc
            if calc > max:
                max = calc 
        return max
    
    def regression(self, col, k):
        res = 0
        for val in col:
            res += col[val]
        return res / k

    def classification(self, col, k):
        copycol1 = {}
        copycol2 = {}

        for i in range(1, k):
            copycol1[i] = col[i]
            copycol2[i] = 0

        for i in copycol1[i]:
            for j in copycol1[i]:
                if i == j:
                    copycol2[i] += 1

        maxi = 0
        for i in copycol2:
            if i > maxi:
                maxi = i
                leMaxi = copycol1[i]

        return leMaxi
    

    def toGraphe(self, col = {}):
        plt.figure('Distances entre A et B')
        col = np.array(list(col.items()))
        plt.clf()
        plt.plot(col, color='blue', marker='o', linestyle='None')
        plt.ylabel('Distance')
        plt.xlabel('Classement')
        plt.savefig('mafig.pdf')

    def normaliser(self, val):
        scaler = MinMaxScaler()
        res = scaler.fit_transform(val)
        return res
    
    def tri(self, col = {}):
<<<<<<< HEAD
        sorte = []
        while bool(col):
            mini = max(col)
            print(col)
            print(mini)
        
        return col
=======
<<<<<<< HEAD
        for i in range(1,len(col)):
            for j in range(1,len(col)):
=======
        for i in range(1, len(col)):
            for j in range(1, len(col)):
>>>>>>> 12490a65a3db1f486fc6a83c106e6e180b570fb3
                if col[j] < col[i]:
                    temp = col[i]
                    col[j] = col[i]
                    col[i] = temp
        return col
    
    
    
    def kMeans(self, x, y):
        # On choisira dans un premier temps $k$ au hasard et on se donne un jeu de données (une matrice où chaque ligne représente une donnée).

        for 

        miniPts = 
        maxiPts = 
        k = random.randint(miniPts, maxiPts)



<<<<<<< HEAD

    def listeToMatr(self, x, y):
        matr = []
        for i in range(len(x)):
            matr.append([x[i], y[i]])
        return matr
    
    

=======
        #Ensuite, Choisir aléatoirement $k$ points,  ces points sont les centres des clusters (appelés aussi centroïd), puis on répète :  
        #1. Affecter chaque point (ligne de  la matrice de données) au groupe dont il est le plus proche (de son centre).  
        #2. Recalculer le centre de chaque cluster et modifier le centroide. On prendra simplement la moyenne des points du cluster.
>>>>>>> 12490a65a3db1f486fc6a83c106e6e180b570fb3
>>>>>>> 4b9a9240cce5531a6e19ee4a3b7d0d05bbd0931c
