from Funciones import generar, semilla
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

CANT_MUESTRAS = 1000
muestra = generar(CANT_MUESTRAS)
valores_x = [] + muestra
valores_y = [] + muestra
valores_z = [] + muestra

del valores_x[0]
del valores_y[len(valores_y)-1]
valores_z.insert(0,semilla)
del valores_z[len(valores_z)-1]
del valores_z[len(valores_z)-1]

valores_y.insert(0,semilla)
del valores_y[len(valores_y)-1]

plt.plot(valores_x, valores_y, 'ro')
plt.show()

ax = plt.axes(projection='3d')
zdata = valores_z
xdata = valores_x
ydata = valores_y
ax.scatter3D(xdata, ydata, zdata)
plt.show()