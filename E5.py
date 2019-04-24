from Funciones import GCL_uniforme
import matplotlib.pyplot as plt

CANT_MUESTRAS = 10000
u = GCL_uniforme(CANT_MUESTRAS)
y = []

for x in range(0,CANT_MUESTRAS):
    if u[x] < 0.4:
        y.append(1)
    else:
        if u[x] < 0.7:
            y.append(2)
        else:
            if u[x] < 0.82:
                y.append(3)
            else:
                if u[x] < 0.92:
                    y.append(4)
                else:
                    y.append(5)

plt.title('Histograma resultado')
plt.hist(y, 5, facecolor='blue', alpha=0.5)
plt.grid(True)
plt.savefig("Histograma-E5.png")
plt.show()