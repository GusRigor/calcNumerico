#Resolvendo o exercio B de compartimentos usando o metodo integrador Runge-Kutta

import math
import matplotlib.pyplot

k12 = 0.03
k20 = 0.01
k21 = 0.02
k31 = 0.08

def kUm1(x1, x2, x3):
    return k31 * x3 + k21 * x2 - k12 * x1

def kDois1(x1, x2, x3, k1):
    return k31 * (x3 + k1/2) + k21 * (x2 + k1/2) - k12 * (x1 + k1/2)

def kTres1(x1, x2, x3, k2):
    return k31 * (x3 + k2/2) + k21 * (x2 + k2/2) - k12 * (x1 + k2/2)

def kQuatro1(x1, x2, x3, k3):
    return k31 * (x3 + k3) + k21 * (x2 + k3) - k12 * (x1 + k3)

def kUm2(x1, x2):
    return k12 * x1 - (k20 + k21) * x2

def kDois2(x1, x2, k1):
    return k12 * (x1 + k1 / 2) - (k20 + k21) * (x2 + k1 / 2)

def kTres2(x1, x2, k2):
    return k12 * (x1 + k2 / 2) - (k20 + k21) * (x2 + k2 / 2)

def kQuatro2(x1, x2, k3):
    return k12 * (x1 + k3) - (k20 + k21) * (x2 + k3)
    
def kUm3(x3):
    return -k31 * x3
    
def kDois3(x3, k1):
    return -k31 * (x3 + k1/2)

def kTres3(x3, k2):
    return -k31 * (x3 + k2/2)

def kQuatro3(x3, k3):
    return -k31 * (x3 + k3)

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

rk31 = 0
rk32 = 0
rk33 = 0
rk34 = 0

x1 = 100
x2 = 10
x3 = 20

auxX1 = 0
auxX2 = 0
auxX3 = 0
erro = 0

matplotlib.pyplot.ioff()

graphT = []
graphX1 = []
graphX2 = []
graphX3 = []

debug = input('Ver passo a passo? [S/N]')

while t < 800:
    auxX1 = x1
    auxX2 = x2
    auxX3 = x3
    
    rk11 = h*kUm1(x1, x2, x3)
    rk21 = h*kUm2(x1, x2)
    rk31 = h*kUm3(x3)

    rk12 = h*kDois1(x1, x2, x3, rk11)
    rk22 = h*kDois2(x1, x2, rk21)
    rk32 = h*kDois3(x3, rk31)

    rk13 = h*kTres1(x1, x2, x3, rk12)
    rk23 = h*kTres2(x1, x2, rk22)
    rk33 = h*kTres3(x3, rk32)

    rk14 = h*kQuatro1(x1, x2, x3, rk13)
    rk24 = h*kQuatro2(x1, x2, rk23)
    rk34 = h*kQuatro3(x3, rk33)

    if debug == 'S':
        print(f't:{t} || x1:{x1} || x2:{x2} || x3:{x3}')

    graphT.append(t)
    graphX1.append(x1)
    graphX2.append(x2)
    graphX3.append(x3)

    x1 = x1 + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
    x2 = x2 + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
    x3 = x3 + (rk31 + 2 * rk32 + 2 * rk33 + rk34)/6
    erro = (x1 - auxX1) / auxX1 + (x2 - auxX2) / auxX2 + (x3 - auxX3) / auxX3
    t = t + h

matplotlib.pyplot.plot(graphT,graphX1,label='x1')
matplotlib.pyplot.plot(graphT,graphX2,label='x2')
matplotlib.pyplot.plot(graphT,graphX3,label='x3')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (x1 e x2 e x3)')
matplotlib.pyplot.title('Exercício Runge-Kutta graph - Gustavo R. BEC'')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


    
    
    

    

    
    


