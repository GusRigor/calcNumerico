#Exe c/ imunidade

import requests
import os
import csv
import math
import matplotlib.pyplot

def kUm1(x1):
    return -1 * k12 * x1

def kDois1(x1, k1):
    return -1 * k12 * (x1 + k1/2)

def kTres1(x1, k2):
    return -1 * k12 * (x1 + k2/2)

def kQuatro1(x1, k3):
    return -1 * k12 * (x1 + k3)

def kUm2(x1, x2):
    return k12 * x1 - (k23 + k24) * x2

def kDois2(x1, x2, k1):
    return k12 * (x1 + k1 / 2) - (k23 + k24) * (x2 + k1 / 2)

def kTres2(x1, x2, k2):
    return k12 * (x1 + k2 / 2) - (k23 + k24) * (x2 + k2 / 2)

def kQuatro2(x1, x2, k3):
    return k12 * (x1 + k3) - (k23 + k24) * (x2 + k3)

def kUm3(x2):
    return k23 * x2
    
def kDois3(x3, k1):
    return k23 * (x2 + k1/2)

def kTres3(x2, k2):
    return k23 * (x2 + k2/2)

def kQuatro3(x2, k3):
    return k23 * (x2 + k3)

def kUm4(x2):
    return k24 * x2
    
def kDois4(x2, k1):
    return k24 * (x2 + k1/2)

def kTres4(x2, k2):
    return k24 * (x2 + k2/2)

def kQuatro4(x2, k3):
    return k24 * (x2 + k3)


def DeltaX(caso):
    return int(caso[len(caso)-1]) - int(caso[len(caso)-2])

def baixar_arquivo(url, endereco=None):
    if endereco is None:
        endereco = 'arquivos/' + os.path.basename(url.split("?")[0])
    resposta = requests.get(url, stream=True)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            for parte in resposta.iter_content(chunk_size=256):
                novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


if __name__ == "__main__":
    # testando a função
    n = 0
    test_url = ["https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv","https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"]
    while n != 3:
        baixar_arquivo(test_url[n])
        n += 1 
        
with open('arquivos/time_series_covid19_confirmed_global.csv', 'r') as arqConfirmados:
    ler = csv.DictReader(arqConfirmados)
    for linha in ler:
        if linha['Country/Region'] == 'Brazil':
            casosConfirmados = linha
casos = []
for e in casosConfirmados.values():
    casos.append(e)
del casos [0]
del casos [0]
del casos [0]
del casos [0]
print(casos)
print(casos[len(casos) - 1])

with open('arquivos/time_series_covid19_recovered_global.csv', 'r') as arqConfirmados:
    ler = csv.DictReader(arqConfirmados)
    for linha in ler:
        if linha['Country/Region'] == 'Brazil':
            RecuperadosCasos = linha
recuperados = []
for e in RecuperadosCasos.values():
    recuperados.append(e)
del recuperados [0]
del recuperados [0]
del recuperados [0]
del recuperados [0]
print(recuperados)
print(recuperados[len(recuperados) - 1])

with open('arquivos/time_series_covid19_deaths_global.csv', 'r') as arqConfirmados:
    ler = csv.DictReader(arqConfirmados)
    for linha in ler:
        if linha['Country/Region'] == 'Brazil':
            mortosConfirmados = linha
mortos = []
for e in mortosConfirmados.values():
    mortos.append(e)
del mortos [0]
del mortos [0]
del mortos [0]
del mortos [0]
print(mortos)
print(mortos[len(mortos) - 1])

Brasil = 209000000 * 0.7 - int(casos[len(casos)-1])

deltaCasos = DeltaX(casos)
deltaMortes = DeltaX(mortos)
deltaRecuperados = DeltaX(recuperados)

k12 = deltaCasos /  Brasil
k23 = deltaMortes / int(casos[len(casos)-1])
k24 = deltaRecuperados / int(casos[len(casos)-1])



print(k12)
print(k23)
print(k24)

print(f'{Brasil:} Pessoas')

h = 1
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

rk41 = 0
rk42 = 0
rk43 = 0
rk44 = 0

x1 = Brasil
x2 = int(casos[len(casos)-1])
x3 = int(mortos[len(mortos)-1])
x4 = int(recuperados[len(recuperados)-1])

auxX1 = 0
auxX2 = 0
auxX3 = 0
auxX4 = 0
erro = 0

matplotlib.pyplot.ioff()

graphT = []
graphX2 = []
graphX3 = []
graphX4 = []

while t < 20:
    auxX1 = x1
    auxX2 = x2
    auxX3 = x3
    auxX4 = x4

    rk11 = h*kUm1(x1)
    rk21 = h*kUm2(x1, x2)
    rk31 = h*kUm3(x2)
    rk41 = h*kUm4(x2)

    rk12 = h*kDois1(x1, rk11)
    rk22 = h*kDois2(x1, x2, rk21)
    rk32 = h*kDois3(x2, rk31)
    rk42 = h*kDois4(x2, rk41)

    rk13 = h*kTres1(x1, rk12)
    rk23 = h*kTres2(x1, x2, rk22)
    rk33 = h*kTres3(x2, rk32)
    rk43 = h*kTres4(x2, rk42)

    rk14 = h*kQuatro1(x1, rk13)
    rk24 = h*kQuatro2(x1, x2, rk23)
    rk34 = h*kQuatro3(x2, rk33)
    rk34 = h*kQuatro4(x2, rk43)

    print(f't:{t} || PP:{x1} || C:{x2} || M:{x3} || R:{x4}')

    graphT.append(t)
    graphX2.append(x2)
    graphX3.append(x3)
    graphX4.append(x4)

    x1 = x1 + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
    x2 = x2 + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
    x3 = x3 + (rk31 + 2 * rk32 + 2 * rk33 + rk34)/6
    x4 = x4 + (rk41 + 2 * rk42 + 2 * rk43 + rk44)/6

    k12 = (x2 - auxX2) / x1
    k23 = (x3 - auxX3) / x2
    k24 = (x4 - auxX4) / x2

    erro = (x1 - auxX1) / auxX1 + (x2 - auxX2) / auxX2 + (x3 - auxX3) / auxX3 + (x4 - auxX4) / auxX4
    t = t + h

matplotlib.pyplot.plot(graphT,graphX2,label='C(t)')
matplotlib.pyplot.plot(graphT,graphX3,label='M(t)')
matplotlib.pyplot.plot(graphT,graphX4,label='R(t)')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (C(t) e M(t) e R(t))')
matplotlib.pyplot.title('Exercício Covid 19 graph - Gustavo R. BEC')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

    

    

