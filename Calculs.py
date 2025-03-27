from math import *
from matplotlib import pylab as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


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

        for i in range(k):
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
        plt.plot(col)
        plt.ylabel('Distance')
        plt.xlabel(r'$\gamma_c$')
        plt.savefig('mafig.pdf')

    def normaliser(self, val):
        scaler = MinMaxScaler()
        res = scaler.fit_transform(val)
        return res
    
    def tri(self, col = {}):
        trie = sorted(col.values())
        return trie

    # skibidi dopamine