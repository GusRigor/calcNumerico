#Exercio para calcular a EDO do valor de um corpo circular em queda livre

#variáveis
m = 1 #massa do corpo em Kg
b = 0.2 #b do corpo em Kg²/s
g = 9.81 #gravidade em m/s²
h = 0.01 #tamanho do passo, neste caso em s
v = [] #vetor onde serão salvas as velocidades
n = 0 #contador para o vetor

Vterm = (m*g/b)**(1/2) #O maior valor que a velocidade poderá chegar

def fx(v,b,m,g,h):
    return v + ((-b)*v**2/m - g)*h

VlrVterm = float(input(f"""Velocidade terminal: {Vterm} m/s,
Qual será a velocidade inicial para o corpo?
[Digite 999 para Velocidade igual a velocidade terminal]
"""))
tst = input('Mostar o passo a passo?[S/N]')
if(VlrVterm == 999):
    VlrVterm = Vterm
    print(f"""A velocidade terminal ocorreu no tempo {n*h} s.""")


v.append(VlrVterm)
if(tst == 'S'):
    print(f'Tempo {n}, Velocidade: {v[n]}')
n = n + 1
v.append(fx(v[n-1],b,m,g,h))
if(tst == 'S'):
    print(f'Tempo {n}, Velocidade: {v[n]}')

while True:
    if(v[n]<0.0):
        break
    if(Vterm > v[n]):
        if(Vterm <v[n-1]):
            print(f"""A velocidade terminal ocorreu no tempo {n*h} s.""")
        
    n = n + 1
    v.append(fx(v[n-1],b,m,g,h))
    if(tst == 'S'):
        print(f'Tempo {n}, Velocidade: {v[n]}')
        
print(f"""A velocidade chegou em Zero no tempo {n*h} s.""")
