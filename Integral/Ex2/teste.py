def d2fx(x):
    cima = -2*(-3**2 - 1)
    baixo = (x**2 - 1)**3
    return cima/baixo
print(d2fx(0.4))

def f(x):
    return -2*(-3**2 - 1)/(x**2 - 1)**3
print(f(0.4))
