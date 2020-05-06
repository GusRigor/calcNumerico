#Exe c/ imunidade

import requests
import os
import csv
import math
import matplotlib.pyplot

def kUm1(x1):
    return - k12 * x1

def kDois1(x1, k1):
    return - k12 * (x1 + k1/2)

def kTres1(x1, k2):
    return - k12 * (x1 + k2/2)

def kQuatro1(x1, k3):
    return - k12 * (x1 + k3)

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
    return int(caso[len(caso)-2]) - int(caso[len(caso)-1])

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

deltaCasos = DeltaX(casos)
deltaMortes = DeltaX(mortos)
deltaRecuperados = DeltaX(recuperados)

k12 = deltaCasos
k23 = deltaMortes / deltaCasos
k24 = deltaRecuperados / deltaCasos

Brasil = 209000000 * 0.7 - int(casos[len(casos)-1])

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


