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
for x in range(0,100000):
        #considero q antes de 20 y despues de 60 ya es 0
        #     x1 = randint(20, 60)
        x1 = random.rand() * 40 + 20
        y = random.random() / 20 
        if y < fx(x1):
                ejeX.append(x1)
                # ejeY.append(fx(x1))
    
print(stats.variance(ejeX))
# plt.scatter(ejeX,ejeY)
plt.figure()
plt.title('Normal de python vs Normal de ejercicio')
plt.subplot(211)
plt.hist(random.normal(40 , 6, 100000),60,label='normal de python')
plt.subplot(212)
plt.hist(ejeX,60, label='histograma del ejercicio')
plt.savefig("Histograma-E4.png")
plt.show()