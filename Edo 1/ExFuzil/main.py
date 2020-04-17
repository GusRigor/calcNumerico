#Este é um programa para calcular a trajetória de uma bala de um fuzil
#Exercício da aula de cálculo numérico ministrada no quinto semestre de
#Engenharia da Computação. Feito por Gustavo Gomes Rigor.
#O fuzil escolhido foi AK47
#Cartucho 5.45x39mm

import math

def convRadius(x):
    return x * math.pi / 180

def mod(x):
    if(x < 0):
        return x * (-1)
    return x

print("""O fuzil selecionado foi o AK-47
utilizando o cartucho 5.45x39mm""")

velocidadeInicial = 900 #m/s
massa = 0.00343 #kg massa do projétil

areaFrontal = 0.25 * math.pi * 0.00545 #metros
roAr = 1.164 #considerando constante
coeficienteArrasto = 0.5 #considerando o projetil um cone
b = coeficienteArrasto * areaFrontal * roAr * 0.5
g = 9.81

ang1 = float(input('Qual o ângulo do fuzil em relação ao solo no disparo?')) #graus
ang = convRadius(ang1) #rad

passo = 0.001 #segundos

n = 0 #contador
altura = 0 #no Y
distancia = 0 #no X

x = [] #posicao de X no tempo
delX = [] #variacao de X no intervalo de tempo
y = [] #posicao de Y no tempo
delY = [] #variacao de Y no intervalo de tempo
v = [] #velocidade do projétil no tempo
Etot = [] #energia do sistema

v.append(velocidadeInicial)
Etot.append(massa * 0.5 * v[n]**2)
x.append(v[n] * math.cos(ang) * passo)
delX.append(x[n] - distancia)
distancia = x[n]
y.append(v[n] * math.sin(ang) * passo)
delY.append(y[n] - altura)
altura = y[n]
ang = math.atan(delY[n]/delX[n])
alturaMax = 0

n = n + 1

while True:
    if(altura < 0.0):
        break
    Etot.append(Etot[n-1] - b * v[n-1]**2 * (delX[n-1] + delY[n-1])) # 1
    v.append(((Etot[n]-massa*g*altura)/(massa*0.5 + b*(delX[n-1] + delY[n-1])))**(1/2)) # 2
    x.append(x[n-1] + v[n-1] * math.cos(ang) * passo) # 3
    y.append(y[n-1] + v[n-1] * math.sin(ang) * passo) # 3
    distancia = x[n] # 3, em tese, não precisa
    altura = y[n] # 3, em ,tese, não precisa
    delX.append(x[n] - x[n-1]) # 4
    delY.append(y[n] - y[n-1]) # 4
    print(delY[n]/delX[n])
    ang = math.atan(delY[n]/delX[n]) # 5
        #if(n>2):
            #if(v[n-1]>v[n]):
                #if(v[n-1]<v[n-1]):
                   # alturaMax = y[n-1]
                   # print(f'Altura máxima: {y[n-1]}')
    print(f"""Tempo: {n*passo} s
Velocidade: {v[n]}
Altura: {altura}
Distância: {distancia}""")
    n = n + 1
print(f"""Para um ângulo {ang1}º
Alcance máximo: {x[n]} m
Altura máxima: {alturamax} m
Em {n*passo} s""")
