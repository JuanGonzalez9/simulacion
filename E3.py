import matplotlib.pyplot as plt
import statistics as stats
from Funciones import generarNormal1

z1 = generarNormal1(100000)

# Histogramas
plt.figure(figsize=(9,6))
plt.title('Z1')
plt.hist(z1,80)
plt.show()
plt.clf()

#Calculo de media y varianza de la muestra
print('Media de la muestra: ',stats.mean(z1))
print('Varianza de la muestra: ',stats.variance(z1))