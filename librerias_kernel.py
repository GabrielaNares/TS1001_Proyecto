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
