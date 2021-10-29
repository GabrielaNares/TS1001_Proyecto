import librerias_kernel as lbk

#Funcion para agregar padding
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    
#Formato de Imagen
Is = Image.open('Sample.png'); #Imagen del perro
I = Is.convert('L'); #Convierte imagen a escala de grises
I = numpy.asarray(I); #Conversion numerica para operar de 0-1
I = I / 255.0; #Normalizacion 0-1

#Se agrega padding
I = numpy.pad(I, 10, pad_with, padder=0)

#Kernel Sombrero
ks=lbk.kernel_sombrero(3,15)

#Kernel Gauss
kg=lbk.gauss(10,15)

#Kernel Laplacian
klp = lbk.Laplacian(5,15)

#Se aplica Kernel Sombrero a Imagen
Imagen = ndimage.convolve(I, ks, mode='constant', cval=0.0)

#Se aplica Kernel Gauss a Imagen
Imagen1 = ndimage.convolve(I, kg, mode='constant', cval=0.0)

#Se aplica Laplacian a Imagen
Imagen2 = ndimage.convolve(I, klp, mode='constant', cval=0.0)

#Se ajusta tamaño de Figura
plt.figure(figsize = (15,15))

#Imagen original 
plt.subplot(3,3,1)
plt.imshow(Is)
plt.xlabel('Input Image')

#Imagen con kernel Sombrero
plt.subplot(3,3,2)
plt.imshow(Imagen)
plt.xlabel('Kernel Sombrero sigma=3')

#Imagen con kernel Gauss
plt.subplot(3,3,3)
plt.imshow(Imagen1)
plt.xlabel('Kernel Gauss sigma = 10')

#Imagen con kernel Laplacian
plt.subplot(3,3,4)
plt.imshow(Imagen2)
plt.xlabel('Kernel Laplacian sigma= 5')

#Imagenes con kernel
plt.subplot(3,3,5)
plt.imshow(Imagen3)
plt.xlabel('Kernel =')


plt.grid(False)
plt.show()
