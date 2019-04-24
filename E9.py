import numpy as np
from Funciones import GCL_uniforme,generar
import matplotlib.pyplot as plt
from scipy.stats import chisquare

cant_muestras = 100000
alfa = 0.20000
beta = 0.50000

unif = GCL_uniforme(cant_muestras)
gaps = np.zeros(cant_muestras)
gap = 0
i =0
while (i < cant_muestras):
    if ((unif[i]<alfa)or(unif[i]>=beta)):
        gap+=1
        i+=1
    else:
        gaps[i]=gap+1
        gap = 0
        i+=1

#Generando las probabilidades esperadas
p = beta - alfa
gapMax = int (np.max(gaps))

plt.hist(gaps, gapMax)
plt.show()

#esperado = np.zeros(cant_muestras)
#for x in range(0,cant_muestras):
 #      esperado[x] = p * ((1-p)**(x))

#test = chisquare(gaps,esperado,0.01)
#print(test)
