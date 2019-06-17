from math import factorial
import random
import matplotlib.pyplot as plt

def numero_combinaciones(m, n):
    """Calcula y devuelve el número de combinaciones
       posibles que se pueden hacer con m elementos
       tomando n elementos a la vez.
    """
    return factorial(m) // (factorial(n) * factorial(m - n))

# para 50 clientes hago una matriz de 51x51
size = 51

mDeTransicion = [[0 for x in range(size)] for y in range(size)] 
p = 0.7

for i in range(size):
    sumatoria = 0.0
    for j in range(size - 1,-1,-1):
        if j >= i:
            mDeTransicion[i][j] = numero_combinaciones(size - 1,j-i) * (p ** (j - i)) * ((1 - p) ** (size - 1 - (j - i)))
            sumatoria += mDeTransicion[i][j]
        else:
            mDeTransicion[i][j] = (1 - sumatoria)
            if i != 1:
                mDeTransicion[i][j] /= (i - 1)

# simulacion
pasos = 100000
posicion = 0 #posicionInicial --> 0 clientes
cantClientes = [posicion]

for j in range(pasos):
    nRandom = random.random()
    suma = 0
    for i in range(size):
        suma += mDeTransicion[posicion][i]
        if suma > nRandom:
            posicion = i
            cantClientes.append(i)
            break

# num_bins = 50
# n, bins, patches = plt.hist(cantClientes, num_bins, facecolor='blue', alpha=0.5)
# plt.savefig("TP2-E2.png",bbox_inches='tight')
# plt.show()

ceros = 0
for i in range(pasos):
    if cantClientes[i] == 0:
        ceros += 1

print("El porcentaje de tiempo sin clientes es ", ceros/pasos)

mayorACuarenta = 0
for i in range(pasos):
    if cantClientes[i] > 40:
        mayorACuarenta += 1

print("El porcentaje de tiempo con mas de 40 clientes es ", mayorACuarenta/pasos)
#da aproximadamente 22% entonces no es recomendable el nuevo servidor

