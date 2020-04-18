#Este é um programa para calcular a trajetória de uma bala de um fuzil
#Exercício da aula de cálculo numérico ministrada no quinto semestre de
#Engenharia da Computação. Feito por Gustavo Gomes Rigor.
#O fuzil escolhido foi AK47
#Cartucho 5.45x39mm

import math

def fy(v,b,m,g):
    return v + ((-b)*v**2/m - g)

def convRadius(x):
    return x * math.pi / 180
def convGraus(x):
    return x * 180 / math.pi

def mod(x):
    if(x < 0):
        return x * (-1)
    return x
def max(a):
    if len(a) <= 1:
        m = a[0]
    else:
        m = a[0]
        for i in range(1,len(a)):
            if a[i]>m:
                m = a[i]

    return m

print("""O fuzil selecionado foi o AK-47
utilizando o cartucho 5.45x39mm""")

velocidadeInicial = 900 #m/s
massa = 0.00343 #kg massa do projétil

areaFrontal = 0.25 * math.pi * 0.00545 #metros
roAr = 1.164 #considerando constante
coeficienteArrasto = 0.5 #considerando o projetil um cone
b = coeficienteArrasto * areaFrontal * roAr * 0.5
g = 9.81
debug = 'S'
dnv = 'S'
while dnv == 'S':
    ang1 = float(input('Qual o ângulo do fuzil em relação ao solo no disparo?')) #graus
    ang = convRadius(ang1) #rad
    debug = input('Quer ver o passo a passo? [S/N]')

    passo = 0.001 #segundos

    n = 0 #contador
    altura = 0 #no Y
    distancia = 0 #no X

    x = [] #posicao de X no tempo
    delX = [] #variacao de X no intervalo de tempo
    y = [] #posicao de Y no tempo
    delY = [] #variacao de Y no intervalo de tempo
    vX = [] #velocidade do projétil no tempo em X
    vY = [] #velocidade do projétil no tempo em Y
    EX = [] #energia em X
    EY = [] #energia em Y

    vX.append(velocidadeInicial * math.cos(ang))
    vY.append(velocidadeInicial * math.sin(ang))

    EX.append(massa * 0.5 * vX[n]**2)
    EY.append(massa * 0.5 * vY[n]**2)

    x.append(vX[n] * passo)
    delX.append(x[n] - distancia)
    distancia = x[n]

    y.append(vY[n] * passo)
    delY.append(y[n] - altura)
    altura = y[n]

    ang = math.atan(delY[n]/delX[n])
    caindo = 0

    n = n + 1

    while True:
        if(vY[n-1] < 0.0001):
            break
        EX.append(EX[n-1] - b * vX[n-1]**2) # 1
        EY.append(EY[n-1] - b * vY[n-1]**2) # 1
        if EX[n] < 0 and (massa*0.5 + b* delX[n-1]) < 0:
            print('Segue o baile')
        if EX[n] < 0 and (massa*0.5 + b* delX[n-1]) > 0:
            print('Deu Ruim X1')
            break
        if EX[n] > 0 and (massa*0.5 + b* delX[n-1]) < 0:
            delX[n-1] = mod(delX[n-1])
            print('Deu Ruim X2, a bala tah indo para tras')   
        vX.append((EX[n]/(massa*0.5 + b* delX[n-1]))**(1/2)) # 2
        
        if((EY[n]) < 0 and (massa*0.5 + b* delY[n-1]) < 0):
            print('Segue o baile')
        if((EY[n]) < 0 and (massa*0.5 + b* delY[n-1]) > 0):
            print('Deu Ruim Y1, acabou a energia em Y')
            break
        if(EY[n]) > 0 and (massa*0.5 + b* delY[n-1]) < 0:
            delY[n-1] = mod(delY[n-1])
            caindo = 1
            print('A bala tah caindo.')
        vY.append(((EY[n])/(massa*0.5 + b* delY[n-1]))**(1/2)) # 2
        
        x.append(x[n-1] + vX[n-1] * passo) # 3
        y.append(y[n-1] + vY[n-1] * passo) # 3
        
        distancia = x[n] # 3, em tese, não precisa
        altura = y[n] # 3, em tese, não precisa
        
        delX.append(x[n] - x[n-1]) # 4
        delY.append(y[n] - y[n-1]) # 4
        if(debug == 'S'):
            print(convGraus(math.atan(delY[n]/delX[n])))
        ang = math.atan(delY[n]/delX[n]) # 5
        if(debug == 'S'):
            print(f"""Tempo: {n*passo} s
    Velocidade em X: {vX[n]}
    Velocidade em Y: {vY[n]}
    Altura: {altura}
    Distância: {distancia}""")
        n = n + 1
    print(f'projetil começou a cair em {n*passo}s')

    x.append(x[n-1] + vX[n-1] * passo) # 3
    vY.append(0)
    y.append(y[n-1] + vY[n-1] * passo) # 3
    distancia = x[n] # 3, em tese, não precisa
    altura = y[n] # 3, em ,tese, não precisa
    delX.append(x[n] - x[n-1]) # 4
    delY.append(delY[n-1]) # 4
    ang = math.atan(delY[n]/delX[n]) # 5

    while True:
        if(altura < 0.001):
            break
        EX.append(EX[n-1] - b * vX[n-1]**2) # 1
        if EX[n] < 0 and (massa*0.5 + b* delX[n-1]) < 0:
            print('Segue o baile')
        if EX[n] < 0 and (massa*0.5 + b* delX[n-1]) > 0:
            print('Deu Ruim X1')
            break
        if EX[n] > 0 and (massa*0.5 + b* delX[n-1]) < 0:
            delX[n-1] = mod(delX[n-1])
            print('Deu Ruim X2, a bala tah indo para tras')   
        vX.append((EX[n]/(massa*0.5 + b* delX[n-1]))**(1/2)) # 2
        vY.append(fy(vY[n-1],b,massa,g)) #2
        x.append(x[n-1] + vX[n-1] * passo) # 3
        y.append(y[n-1] + vY[n-1] * passo) # 3
        distancia = x[n] # 3, em tese, não precisa
        altura = y[n] # 3, em tese, não precisa
        delX.append(x[n] - x[n-1]) # 4
        delY.append(y[n] - y[n-1]) # 4

        if(delY[n] > 0.0 and delX[n] > 0.0):
            if(debug == 'S'):
                print(convGraus(math.atan(delY[n]/delX[n])))
            ang = math.atan(delY[n]/delX[n]) # 5
        if(debug == 'S'):
            print(f"""Tempo: {n*passo} s
    Velocidade em X: {vX[n]}
    Velocidade em Y: {vY[n]}
    Altura: {altura}
    Distância: {distancia}""")
        n = n + 1
        
    alturaMax = max(y)
    print(f"""Para um ângulo {ang1}º
Alcance máximo: {x[n]} m
Altura máxima: {alturaMax} m
Em {n*passo} s""")
    dnv = input('Rodar novamente? [S/N]')
print('Feito por Gustavo G. Rigor')
print('FIM')

