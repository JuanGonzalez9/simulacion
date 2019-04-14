import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

c = 1664525
a = 1013904223
m = 2**32

juan = 92169
dalma = 92257
ema = 94773

semilla = (juan * 0.15) + (dalma * 0.25) + (ema * 0.6)

secuencia = []
secuencia2 = []

for x in range(0, 100000):
    semilla = (a * semilla + c) % m 
    secuencia.append(semilla / m)

# print(secuencia)
# for x in range(0, 10000):
#     print(float(secuencia[x]) / m)

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 40
n, bins, patches = plt.hist(secuencia, num_bins, facecolor='blue', alpha=0.5)
plt.show()