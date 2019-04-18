def generar(N):
    c = 1664525
    a = 1013904223
    m = 2**32
    juan = 92169
    dalma = 92257
    ema = 94773
    semilla = int((juan * 0.15) + (dalma * 0.25) + (ema * 0.6))
    secuencia = []
    for x in range(0, N):
        semilla = (a * semilla + c) % m 
        secuencia.append(semilla)
    return secuencia

def GCL_uniforme(N):
    m = 2 ** 32
    valores = generar(N)
    valores2 = [ x / m for x in valores ]
    return valores2