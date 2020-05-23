#Este é um programa para calcular a corrente em um neurônio
#Modelo de Hodgkin e Huxlei

import matplotlib.pyplot
import math

def alphaN(v):
    return (0.01 * (v - 10)) / (math.exp((v - 10)/10)-1)

def betaN(v):
    return 0.125 * math.exp(v/80)

def alphaM(v):
    return (0.1 * (v - 25)) / (math.exp((v - 25)/10)-1)

def betaM(v):
    return 4 * math.exp(v/18)

def alphaH(v):
    return 0.07 * math.exp(v/20)

def betaH(v):
    return 1 / (math.exp( (v-30) / 10) + 1)

def dNdT(n, v, t = 0.01 * 10**(-3)):
    return n + t * (alphaN(v) * (1 - n) - betaN(v) * n)

def dMdT(m, v, t = 0.01 * 10**(-3)):
    return m + t * (alphaM(v) * (1 - m) - betaM(v) * m)

def dHdT(h, v, t = 0.01 * 10**(-3)):
    return h + t * (alphaH(v) * (1 - h) - betaH(v) * h)

again = 'S'

while again == 'S': 
    print('''Modelo de Hodgkin e Huxlei
Feito por: Gustavo G. Rigor
Onde é utilizado ∆t = 0.01 ms
Dentro do intervalo de [0, 0.25] ms
Caso deseje alterar ∆t aparte S''')
    AAA = input()


    gK = 3.60
    gNa = 12.0
    gL = 0.03

    vK = -77 * 10**(-3) #mV
    vNa = 50 * 10**(-3) #mV
    vL = -54.402 * 10**(-3) #mV

    n0 = 0.3176
    m0 = 0.0529
    h0 = 0.5961

    auxN = n0
    auxM = m0
    auxH = h0

    v0 = -65.002  * 10**(-3) #mV
    t0 = 0 #segundos

    if AAA == 'S':
        dT = float(input('Valor para ∆t em ms')) * 10**(-3) #ms
    else:    
        dT = 0.01 * 10**(-3) #ms
    Cm = 1 * 10**(-6) #µF
    gama = dT/Cm

    tensao = []
    tempo = []
    tempo.append(t0)
    tensao.append(v0)

    pN = gK * (n0**4) * (tensao[0] - vK)
    pM = gNa * (m0**3) * h0 * (tensao[0] - vNa)
    pL = gL * (tensao[0] - vL)

    aux = tensao[0] - (pN + pM + pL) * gama
    tensao.append(aux)
    tempo.append(t0+dT)

    #print(tensao[1])

    M = [m0]
    M.append(m0)
    N = [n0]
    N.append(n0)
    H = [n0]
    H.append(h0)

    i = 0.0
    c = 1

    txt = input('Caso deseje alterar ∆t aparte S')
    if txt == 'S':
        parada = float(input('Valor para tF em ms')) * 10**(-3) #ms 
    else:
        parada = .25*10**(-3)

    while i <= parada:
        auxN = dNdT(auxN, tensao[c])
        N.append(auxN)
        auxM = dMdT(auxM, tensao[c])
        M.append(auxM)
        auxH = dHdT(auxM, tensao[c])
        H.append(auxH)

        pN = gK * (auxN**4) * (tensao[c] - vK)
        pM = gNa * (auxM**3) * auxH * (tensao[c] - vNa)
        pL = gL * (tensao[c] - vL)

        aux = tensao[0] - (pN + pM + pL) * gama
        tensao.append(aux)
     
        c += 1
        i = i + dT
        tempo.append(i)

    #print(tensao)

    matplotlib.pyplot.ioff()
    matplotlib.pyplot.plot(tempo,tensao,label='V(t) V')
    #matplotlib.pyplot.plot(tempo,N,label='N(t)')
    #matplotlib.pyplot.plot(tempo,M,label='M(t)')
    #matplotlib.pyplot.plot(tempo,H,label='H(t)')
    matplotlib.pyplot.xlabel('tempo (t) s')
    matplotlib.pyplot.ylabel('valores (V(t))')
    matplotlib.pyplot.title('Prova 2 Modelo H-H graph - Gustavo R. BEC')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()

    print('Rodar novamente? [S/N]')
    again = input()
