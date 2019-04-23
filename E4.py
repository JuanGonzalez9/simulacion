from numpy import pi,sqrt,random,exp
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as sp
from random import randint
import statistics as stats

def fx(x):
    return a * exp(- ((x - 40)**2) / 72 )

#usamos y exponencial
# sacado del github de la materia
c = sqrt(2*exp(1)/pi)
a = (1 / 6 * sqrt(2 * pi))



ejeX = []
ejeY = []
for x in range(0,10000):
    #considero q antes de 20 y despues de 60 ya es 0
    x1 = randint(20, 60)
    y = random.random() / 20 
    if y < fx(x1):
        ejeX.append(x1)
        ejeY.append(fx(x1))

print(stats.variance(ejeX))
plt.scatter(ejeX,ejeY)
plt.show()