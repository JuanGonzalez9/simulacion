from math import factorial

def numero_combinaciones(m, n):
    """Calcula y devuelve el número de combinaciones
       posibles que se pueden hacer con m elementos
       tomando n elementos a la vez.
    """
    return factorial(m) // (factorial(n) * factorial(m - n))

size = 50
mDeTransicion = [[0 for x in range(size)] for y in range(size)] 
p = 0.7

for i in range(size):
    sumatoria = 0.0
    for j in range(49,-1,-1):
        if j >= i:
            mDeTransicion[i][j] = numero_combinaciones(50,j-i) * (p ** (j - i)) * ((1 - p) ** (50 - j - i))
            sumatoria += mDeTransicion[i][j]
        else:
            mDeTransicion[i][j] = (1 - sumatoria)
            if i != 1:
                mDeTransicion[i][j] /= (i - 1)

# print(mDeTransicion[2])
print(numero_combinaciones(50,30))

