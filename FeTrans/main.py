boltz = 5.67 * 10**(-8) # w/m2K4
h = 5 #w/m2K
p = 0.9
e = 0.15
T_Amb = 300 #K
Q_recebe = 900 #W/m2

def diferenca(T):
    return p * Q_recebe - (e * boltz * T**4 + h*(T - T_Amb))

#print(diferenca(400))
Tini = 400
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
