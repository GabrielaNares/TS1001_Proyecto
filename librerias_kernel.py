import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage
 
def kernel_sombrero(sigma,k):
    matrix=numpy.zeros((k,k));
    for x in range (0,k):
        for y in range (0,k):
            matrix[x][y]=1/(numpy.pi*sigma**4)*(1-1/2*(x**2+y**2)/sigma**2)
            matrix[x][y]= matrix[x][y] * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return matrix

def gauss(sigma,k):
    g=numpy.zeros((k,k));
    for x in range (0,k):
        for y in range (0,k):
            g[x][y]=1/(2*numpy.pi*sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return g

   def Laplacian(sigma, k):
    matix=[[0] * k for i in range(k)]
    for i in range(k):
        for j in range(k):
            matrix[i][j]=((x**2+y**2-2*sigma**2)/sigma**4)*math.exp(-1*(x**2+y**2)/2*sigma**2)(i-(k-1)/2,j-(k-1)/2,sigma)
    return matrix
