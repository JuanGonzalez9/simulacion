import matplotlib.pyplot as plt
import statistics as stats
from Funciones import generarNormal1
from scipy.stats import kstest

z1 = generarNormal1(100000)

test = kstest(z1,'norm')

print(test)
# da entre 0.001 y 0.003. Me fijo en las tablas
#  y con el n = 100000 y cualquier alfa me da que se acepta