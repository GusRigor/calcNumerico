import math

def radiusToDegree(x):
    return x * 57.2958


def ordemErro(x, h):
    return (h**2/2) * -1*math.cos(x) + (h**3/6) * math.sin(x) + (h**4/24) * math.cos(x)

def fx(x):
    return math.cos(x)

def dFdX(h):
    print(f'h = {h}')
    print('Diferenças Progressivas:')

    dfdx = -10 * ( ( fx(x+h) - fx(x) ) / h + ordemErro(x, h) )
    print(f'df/dx = {dfdx}')
    print(f'ER% = {(r-dfdx)*100/r} %')

    print('Diferenças Atrassada:')
    dfdx = -10 * ( ( fx(x) - fx(x-h) ) / h + ordemErro(x, h) )
    print(f'df/dx = {dfdx}')
    print(f'ER% = {(r-dfdx)*100/r} %')


    print('Diferenças Centrais:')
    dfdx = -10 * ( ( fx(x+h) - fx(x-h) ) / 2*h + (10*ordemErro(x, h))**2 )
    print(f'df/dx = {dfdx}')
    print(f'ER% = {(1-(r-dfdx)/r)*100} %')
    print()




pi = math.pi
x = pi/6
x = radiusToDegree(x)
r= 10*math.sin(x)
h1 = 0.1
h2 = 0.02
h3 = 0.0001

print('Resultados das derivadas para o cálculo de diferenças parciais de f(x) = 10cos(x)')
print('x = π/6')
print(f'Real: {r}')

dFdX(h1)
dFdX(h2)
dFdX(h3)
