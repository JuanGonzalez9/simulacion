from numpy import random, log 
import matplotlib.pyplot as plt
import statistics as stats
#Generar muestras de una v.a. exponencial a partir
#de una distribucion uniforme [0,1]
#utilizando el metodo de la transformacion inversa

cantMuestras = 100000
#parametro de distribucion exponencial
#como piden que la media sea 20 lambda debe ser 1/20
l = 1/20

# Muestras de la variable uniforme
u = random.rand(cantMuestras)

#Histograma de la muestra uniforme
plt.figure()
plt.subplot(121)
plt.title('Histograma de U')
plt.hist(u)
plt.grid(True)

#transformacion inversa
x = -log(1-u) / l

#media
print('Media de la muestra: ',stats.mean(x))
#Varianza 
print('Varianza de la muestra: ',stats.variance(x))
print('Varianza de la muestra: ',stats.pvariance(x))
#Histograma resultado
plt.subplot(122)
plt.title('Histograma de X')
plt.hist(x,100)
plt.grid(True)
plt.show()