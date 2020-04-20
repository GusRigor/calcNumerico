#exemplo de aplicacao de integracao numerica Runge Kutta
import math
import matplotlib.pyplot

def kUm1(t, c, a):
    return c / (math.exp(t)-1) + 2 * math.sin(t) * a / (math.cos(t) * (1 + math.exp(-t)))

def kDois1(t, c, a, k1, h):
    return (c + k1 / 2) / (math.exp(t + h / 2) - 1) + 2 * math.sin(t + h / 2) * (a + k1 / 2) / (math.cos(t + h / 2) * (1 + math.exp(-(t + h / 2))))


def kTres1(t, c, a, k2, h):
    return (c + k2 / 2) / (math.exp(t + h / 2) - 1) + 2 * math.sin(t + h / 2) * (a + k2 / 2) / (math.cos(t + h / 2) * (1 + math.exp(-(t + h / 2))))

def kQuatro1(t, c, a, k3, h):
    return (c + k3) / (math.exp(t + h / 2) - 1) + 2 * math.sin(t + h / 2) * (a + k3) / (math.cos(t + h / 2) * (1 + math.exp(-(t + h / 2))))
    
def kUm2(t, c, a):
    return 2 * a / (math.exp(2 * t) - 1) - 2 * (1 + math.exp(-t)) * math.cos(t) * c / math.sin(t)

def kDois2(t, c, a, k1, h):
    return 2 * (a + k1 / 2) / (math.exp(2 * (t + h / 2)) - 1) - 2 * (1 + math.exp(-(t + h / 2))) * math.cos(t + h / 2) * (c + k1 / 2) / math.sin(t + h / 2)

def kTres2(t, c, a, k2, h):
    return 2 * (a + k2 / 2) / (math.exp(2 * (t + h / 2)) - 1) - 2 * (1 + math.exp(-(t + h / 2))) * math.cos(t + h / 2) * (c + k2 / 2) / math.sin(t + h / 2)

def kQuatro2(t, c, a, k3, h):
    return 2 * (a + k3) / (math.exp(2 * (t + h / 2)) - 1) - 2 * (1 + math.exp(-(t + h / 2))) * math.cos(t + h / 2) * (c + k3) / math.sin(t + h / 2)

h = 0.001
t = 0.1
k11 = 0
k12 = 0
k13 = 0
k14 = 0
k21 = 0
k22 = 0
k23 = 0
k24 = 0
c = 0.94845796
a = 179.4625887
auxa = 0
auxc = 0
erro = 0


matplotlib.pyplot.ioff()

graphT = []
graphA = []
graphC = []

debug = input('Ver passo a passo? [S/N]')

while t<4:
    auxa = a
    auxc = c
    k11 = h*kUm1(t, c, a)
    k21 = h*kUm2(t, c, a)
    
    k12 = h*kDois1(t, c, a, k11, h)
    k22 = h*kDois2(t, c, a, k21, h)

    k13 = h*kTres1(t, c, a, k12, h)
    k23 = h*kTres2(t, c, a, k22, h)

    k14 = h*kQuatro1(t, c, a, k13, h)
    k24 = h*kQuatro2(t, c, a, k23, h)
    if debug == 'S':
        print(f't:{t} || c:{c} || a:{a}')

    graphT.append(t)
    graphA.append(a)
    graphC.append(c)

    c = c + (k11 + 2 * k12 + 2 * k13 + k14) / 6
    a = a + (k21 + 2 * k22 + 2 * k23 + k24) / 6
    erro = (a - auxa) / auxa + (c - auxc) / auxc
    t = t + h

matplotlib.pyplot.plot(graphT,graphC,label='c')
matplotlib.pyplot.plot(graphT,graphA,label='a')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (c e a)')
matplotlib.pyplot.title('Runge Kutta graph')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
    
