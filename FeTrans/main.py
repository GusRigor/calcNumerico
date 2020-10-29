boltz = 5.67 * 10**(-8) # w/m2K4
h = 30 #w/m2K
p = 0.85
e = 0.15
T_Amb = 286 #K
Q_recebe = 1000 #W/m2

def diferenca(T):
    return p * Q_recebe - (e * boltz * T**4 + h*(T - T_Amb))

print(diferenca(100))
Tini = 100
passo = 1

T = Tini
while True:
    d = diferenca(T)
    if d < 0:
        break
    #print(f'Temperatura: {T}, Diferenca: {d}')
    T += passo
    
T -= passo
passo = 0.0001

while True:
    d = diferenca(T)
    if d < 0:
        break
    #print(f'Temperatura: {T}, Diferenca: {d}')
    T += passo

T -= passo
passo = passo * passo
while True:
    d = diferenca(T)
    if d < 0:
        break
    #print(f'Temperatura: {T}, Diferenca: {d}')
    T += passo

T -= passo
d = diferenca(T)

print('ADO 6 - Exercício 3 - Gustavo Gomes Rigor')
print(f'Temperatura: {T} K, Diferenca: {d}')
print(f'Temperatura: {T-273.15} ºC')

#print(diferenca(412.66))
#print(412.66-273.15)
