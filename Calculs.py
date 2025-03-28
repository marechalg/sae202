from math import *
from matplotlib import pylab as plt
import numpy as np
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.cluster import KMeans

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
        plt.plot(col, color='blue', marker='o', linestyle='None')
        plt.ylabel('Distance')
        plt.xlabel('Classement')
        plt.savefig('mafig.pdf')

    def normaliser(self, val):
        scaler = MinMaxScaler()
        res = scaler.fit_transform(val)
        return res
    
    def tri(self, col = {}):
        for i in range(1, len(col)):
            for j in range(1, len(col)):
                if col[j] < col[i]:
                    temp = col[i + 1]
                    col[j] = col[i]
                    col[i] = temp
        return col
    
    def kMeans(self, col = {}):
        k = 2  
        max_iters = 10  

        np.random.seed(42)

        col_array = np.array(list(col.values()))

        centroids = col_array[np.random.choice(len(col_array), k, replace=False)]

        for iteration in range(max_iters):
            clusters = [[] for _ in range(k)]
            for point in col:
                distances = [np.linalg.norm(point - centroid) for centroid in centroids]
                closest_cluster = np.argmin(distances)
                clusters[closest_cluster].append(point)
            clusters = [np.array(cluster) for cluster in clusters]
            for i, cluster in enumerate(clusters):
                print(f"Cluster {i}: {cluster.tolist()}")
            new_centroids = np.array([cluster.mean(axis=0) if len(cluster) > 0 else centroids[i] for i, cluster in enumerate(clusters)])
            centroids = new_centroids  

        col = np.array(col)
        plt.scatter(col[:], col[:], c='gray', label='Données')
        plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', label='Centroïdes finaux')
        plt.legend()
        plt.show()

#    test très sérieux