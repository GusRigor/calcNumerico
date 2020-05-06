#Exe c/ imunidade

import requests
import os
import csv
import math
import matplotlib.pyplot

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
print(f'{Brasil} + Pessoas')




