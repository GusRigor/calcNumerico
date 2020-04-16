#Calculando a integral numérica da funcao
# f(x) = 1/(xˆ2)-1 no intervalo 0 a 0.8
#Pelo método do trapézio

def fx(x):
    return 1/((x**2)-1)

def d2fx(x):
    return -2*(-3**2 - 1)/(x**2 - 1)**3

def area(a,b):
    return (fx(a) + fx(b))*(b-a)*0.5

def max(a, b, inc):
    maior = -999
    temp = 0
    while True:
        if(a >= b):
            break
        temp = d2fx(a)
        if(temp > maior):
            maior = temp
        a = a + inc
    return maior

def erro(a,b, n):
    return ((b-a)**3) * max(a, b, 0.01) * (1/(12*(n**2)))

#Funcao para o modulo
def mod(x):
    if(x < 0):
        return x * (-1)
    return x
#Termino da funcao

n = 8 #num de divisoes1
n1 = 800 #num de divisoes2
ini = 0.0
fim = 0.8
wdiv = 0.1 #tamanho de cada passo
wdiv1 = 0.001

a = ini 
b = ini + wdiv
resultado = 0
while True:
    if(a >= fim):
        break
    resultado = resultado + area(a,b)
    a = b
    b = b + wdiv   
#fim do laco e resultado tera o valor aproximado  da integral
print('Para divisoes com tamanho h = 0.1')
print(f'A integral de f(x): {resultado}')
e = mod(erro(ini, fim, n))
print(f'O erro é de: {e}')
print()

a = ini 
b = ini + wdiv1
resultado = 0
while True:
    if(a >= fim):
        break
    resultado = resultado + area(a,b)
    a = b
    b = b + wdiv1  
#fim do laco e resultado tera o valor aproximado  da integral
print('Para divisoes com tamanho h = 0.001')
print(f'A integral de f(x): {resultado}')
e = mod(erro(ini, fim, n1))
print(f'O erro é de: {e}')
    
