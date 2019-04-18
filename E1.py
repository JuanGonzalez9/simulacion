import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import statistics as stats
from Funciones import GCL_uniforme,generar

c = 1664525
a = 1013904223
m = 2**32

juan = 92169
dalma = 92257
ema = 94773

semilla = (juan * 0.15) + (dalma * 0.25) + (ema * 0.6)

valores = generar(5)
print(valores)
valores2 = GCL_uniforme(100000)



print('Media de la muestra: ',stats.mean(valores2))

num_bins = 40
n, bins, patches = plt.hist(valores2, num_bins, facecolor='blue', alpha=0.5)
plt.show()