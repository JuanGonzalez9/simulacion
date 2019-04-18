from numpy import random, sqrt, log, cos, sin, pi
import matplotlib.pyplot as plt
import statistics as stats

# Variables iniciales
cantMuestras = 50000
# Dos variables aleatorias independientes uniformemente
# distribuidas en (0, 1]
u1 = random.rand(cantMuestras)
u2 = random.rand(cantMuestras)
#print(u1)
#print(u2)

# Transformacion a variables con distribucion normal
def aNormales(u1, u2):
    z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
    z2 = sqrt(-2*log(u1))*sin(2*pi*u2)
    return z1,z2

z1,z2 = aNormales(u1,u2)

# Histogramas
plt.figure()
plt.subplot(231) 
plt.title('U1')
plt.hist(u1)      
plt.grid(True)
plt.subplot(232)
plt.title('U2')
plt.hist(u2)
plt.subplot(233) 
plt.title('Z1')
plt.hist(z1)     
plt.subplot(234)
plt.title('Z2')
plt.hist(z2)

z3 = z1+z2
plt.subplot(235)
plt.title('Z3')
plt.hist(z3,80)
plt.show()
plt.clf()

#Calculo de media y varianza de la muestra
print('Media de la muestra: ',stats.mean(z3))
print('Varianza de la muestra: ',stats.variance(z3))