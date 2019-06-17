import matplotlib.pyplot as plt
import statistics as stats
from Funciones import generarNormal1

z1 = generarNormal1(100000)

# Histogramas
plt.figure(figsize=(9,6))
plt.title('Histograma de Z Normal(0,1)')
plt.hist(z1,80,facecolor='blue', alpha=0.5)
plt.savefig("Histograma-E3.png",bbox_inches='tight')
plt.show()
plt.clf()

#Calculo de media y varianza de la muestra
print('Media de la muestra: ',stats.mean(z1))
print('Varianza de la muestra: ',stats.variance(z1))