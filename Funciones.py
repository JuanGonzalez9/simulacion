from numpy import random, sqrt, log, cos, sin, pi

juan = 92169
dalma = 92257
ema = 94773
semilla = int((juan * 0.15) + (dalma * 0.25) + (ema * 0.6))

def generar(N):
    global semilla
    c = 1664525
    a = 1013904223
    m = 2**32
    secuencia = []
    _semilla = semilla
    for x in range(0, N):
        _semilla = (a * _semilla + c) % m 
        secuencia.append(_semilla)
    return secuencia

def GCL_uniforme(N):
    m = 2 ** 32
    valores = generar(N)
    valores2 = [ x / m for x in valores ]
    return valores2
# Con metodo Box-Muller. Ejercicio 3
def generarNormal1(CANT_MUESTRAS):
    # Dos variables aleatorias independientes uniformemente
    # distribuidas en (0, 1]
    u1 = random.rand(CANT_MUESTRAS)
    u2 = random.rand(CANT_MUESTRAS)
    #print(u1)
    #print(u2)

    # Transformacion a variables con distribucion normal
    #z1 v.a. Normales (0,1)
    z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
    return z1