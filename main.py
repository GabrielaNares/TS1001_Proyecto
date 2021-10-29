import librerias_kernel as lbk

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    
Is = Image.open('Sample.png');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;
I = numpy.pad(I, 10, pad_with, padder=0)
        
km=lbk.kernel_sombrero(3,15)

#Sombrero de Kernel
Imagen = ndimage.convolve(I, km, mode='constant', cval=0.0)

#Kernels Gauss
Imagen1 = ndimage.convolve(I, kg, mode='constant', cval=0.0)



plt.figure(figsize = (15,15))

#Imagen original 
plt.subplot(3,3,1)
plt.imshow(Is)
plt.xlabel('Input Image')

#Imagenes de Sombrero
plt.subplot(3,3,2)
plt.imshow(Imagen)
plt.xlabel('Sombrero sigma=3')

plt.subplot(3,3,3)
plt.imshow(Imagen1)
plt.xlabel('Gauss sigma = ')

plt.subplot(3,3,4)
plt.imshow(J3)
plt.xlabel('Mexican Hat sigma=7')

#Imagenes de Gauss
plt.subplot(3,3,5)
plt.imshow(J4)
plt.xlabel('Gauss sigma=3')

plt.subplot(3,3,6)
plt.imshow(J5)
plt.xlabel('Gauss sigma=5')

plt.subplot(3,3,7)
plt.imshow(J6)
plt.xlabel('Gauss sigma=7')

#Imagen Sepia
plt.subplot(3,3,8)
plt.imshow(ks)
plt.xlabel('Kernel Sepia')


#plt.subplot(2,2,4)
#plt.imshow(J2)
#plt.xlabel('Vertical direction')

plt.grid(False)
plt.show()
