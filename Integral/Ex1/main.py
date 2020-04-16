#Calculando a integral numérica da funcao
# f(x) = (6x -5)ˆ1/2 no intervalo 1 a 9
#Pelo método do trapézio

#Definindo a funcao a ter sua integral calculada
def fx(x):
    return (6*x-5)**(1/2)
#Termino da funcao

#Definindo a funcao a ter sua integral calculada
def d2fx(x):
    return 9/(6*x-5)**(3/2)
#Termino da funcao

#print(25**1/2)

#Definindo a funcao da Area do trapezio
def area(a,b):
    return (fx(a) + fx(b))*(b-a)*0.5
#Termino da funcao

#Definindo a funcao Max
def max(a, b, inc):
    maior = 0
    temp = 0
    while True:
        if(a >= b):
            break
        temp = d2fx(a)
        if(temp > maior):
            maior = temp
        a = a + inc
    return maior
#Termino da funcao

#Funcao para o calculo do erro
def erro(a,b, n):
    return ((b-a)**3) * max(a, b, 0.01) * (1/(12*(n**2)))
#Termino da funcao

#Funcao para o modulo
def mod(x):
    if(x < 0):
        return x * (-1)
    return x
#Termino da funcao

n = 100 #num de divisoes
ini = 1.0
fim = 9.0
wdiv = (fim - ini)/ n #tamanho de cada passo
print(f'tamanho do passo {wdiv}')

#calculando o erro dessa funcao

#Termino do calculo do erro

a = ini 
b = ini + wdiv
#print(a, b)
#print(area(1,9))
resultado = 0
c = 0
while True:
    if(a >= fim):
        break
    resultado = resultado + area(a,b)
    a = b
    b = b + wdiv
    c = c + 1
    
#fim do laco e resultado tera o valor aproximado  da integral
print(f'A integral de f(x): {resultado*-1}')
#print(c)
e = mod(erro(ini, fim, n))
print(f'O erro é de: {e}')
    
