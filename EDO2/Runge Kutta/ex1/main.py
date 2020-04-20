#Resolvendo o exercio a de compartimentos usando o metodo integrador Runge-Kutta

import math
import matplotlib.pyplot

k12 = 0.03
k20 = 0.01
k21 = 0.02

def kUm1(x1, x2):
    return k21 * x2 - k12 * x1

def kDois1(x1, x2, k1):
    return k21 * (x2 + k1/2) - k12 * (x1 + k1/2)

def kTres1(x1, x2, k2):
    return k21 * (x2 + k2/2) - k12 * (x1 + k2/2)

def kQuatro1(x1, x2, k3):
    return k21 * (x2 + k3) - k12 * (x1 + k3)

def kUm2(x1, x2):
    return k12 * x1 - (k20 + k21) * x2

def kDois2(x1, x2, k1):
    return k12 * (x1 + k1 / 2) - (k20 + k21) * (x2 + k1 / 2)

def kTres2(x1, x2, k2):
    return k12 * (x1 + k2 / 2) - (k20 + k21) * (x2 + k2 / 2)

def kQuatro2(x1, x2, k3):
    return k12 * (x1 + k3) - (k20 + k21) * (x2 + k3)

h = 0.001
t = 0

rk11 = 0
rk12 = 0
rk13 = 0
rk14 = 0

rk21 = 0
rk22 = 0
rk23 = 0
rk24 = 0

x1 = 100
x2 = 10
auxX1 = 0
auxX2 = 0
erro = 0

matplotlib.pyplot.ioff()

graphT = []
graphX1 = []
graphX2 = []

debug = input('Ver passo a passo? [S/N]')

while t < 570:
    auxX1 = x1
    auxX2 = x2
    
    rk11 = h*kUm1(x1, x2)
    rk21 = h*kUm2(x1, x2)

    rk12 = h*kDois1(x1, x2, rk11)
    rk22 = h*kDois2(x1, x2, rk21)

    rk13 = h*kTres1(x1, x2, rk12)
    rk23 = h*kTres2(x1, x2, rk22)

    rk14 = h*kQuatro1(x1, x2, rk13)
    rk24 = h*kQuatro2(x1, x2, rk23)

    if debug == 'S':
        print(f't:{t} || x1:{x1} || x2:{x2}')

    graphT.append(t)
    graphX1.append(x1)
    graphX2.append(x2)

    x1 = x1 + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
    x2 = x2 + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
    erro = (x1 - auxX1) / auxX1 + (x2 - auxX2) / auxX2
    t = t + h

matplotlib.pyplot.plot(graphT,graphX1,label='x1')
matplotlib.pyplot.plot(graphT,graphX2,label='x2')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (x1 e x2)')
matplotlib.pyplot.title('Exercício Runge-Kutta graph')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


    
    
    

    

    
    


