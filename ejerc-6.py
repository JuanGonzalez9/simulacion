import numpy as np 
import matplotlib.pyplot as plt
# Generar numeros aleatorios en un circulo de radio 1
# a partir de dos muestras
# uniformes [-1, 1]

muestra = 1000
# muestras uniformes [-1, 1]
x = np.random.uniform(-1,1,muestra)
y = np.random.uniform(-1,1,muestra)

#Circulo de radio 1
interior = (x ** 2 + y **2)<=1
exterior = np.invert(interior)
#Grafico
plt.xlim(-2, 2)
plt.ylim(-2, 2)
#plt.scatter(x[interior],y[interior])
plt.plot(x[interior], y[interior], 'b.')
#plt.plot(x[exterior], y[exterior], 'r.')
plt.title('Circulo de radio 1')
plt.grid(True)

plt.show()
plt.clf()
