from Funciones import GCL_uniforme
import matplotlib.pyplot as plt
from scipy.stats import chisquare

CANT_MUESTRAS = 10000
u = GCL_uniforme(CANT_MUESTRAS)
y = [0,0,0,0,0]
z = [4000,3000,1200,1000,800]

for x in range(0,CANT_MUESTRAS):
    if u[x] < 0.4:
        y[0] += 1
    else:
        if u[x] < 0.7:
            y[1] += 1
        else:
            if u[x] < 0.82:
                y[2] += 1
            else:
                if u[x] < 0.92:
                    y[3] += 1
                else:
                    y[4] += 1

test = chisquare(y,z,4)
#fijandome en una tabla, para 4 grados de libertad, con 3.47 que me da el chi2,
#  esta aceptadisimo
print(test)