import random
import numpy as np


tLlegada = []
t = random.expovariate(1.0 / 250)
tLlegada.append(t)

cantInstrucciones = 1000

for x in range(cantInstrucciones - 1):
    t = random.expovariate(1.0 / 250)
    # t + tiempo anterior
    tLlegada.append(t + tLlegada[x])

tiempoTotal = 0
tasaDeEjecucion = 60

for x in range(cantInstrucciones):
    tipoInstruccion = random.random()
    if tipoInstruccion < 0.6:
        tasaDeEjecucion = 60
    else:
        tasaDeEjecucion = 10

    tEjecucion = random.expovariate(1.0 / tasaDeEjecucion)

    randMemoria = random.random()
    if randMemoria < 0.65:
        # alternativa 1 --> 1320 k aprox
        # tEjecucion += random.expovariate(1.0 / 2000)

        # alternativa 2 --> 640 k aprox
        enCache = random.random()
        if enCache < 0.6:
            tEjecucion += random.expovariate(1.0 / 500)
        else:
            tEjecucion += random.expovariate(1.0 / 1500)

    tiempoTotal = max(tLlegada[x],tiempoTotal) + tEjecucion

print(tiempoTotal)
print("jajaja")


