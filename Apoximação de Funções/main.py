import matplotlib.pyplot

def somatorio1(X):
    count = len(X)
    c = 0
    aux = 0
    while True:
        if c == count:
            break
        aux += X[c]
        c+=1
    return aux

def somatorio2(X, Y):
    count = len(X)
    c = 0
    aux = 0
    while True:
        if c == count:
            break
        aux += X[c]*Y[c]
        c+=1
    return aux

def montaGX(G, X, A, B):
    count = len(X)
    c = 0
    while True:
        if c == count:
            break
        G.append( B * X[c] + A)
        c+=1
    return G

def residuo2(F, G):
    count = len(F)
    c = 0
    aux = 0
    while True:
        if c == count:
            break
        aux += (F[c] - G[c])**2
        c+=1
    return aux
        

dadosIBGE = input('Usar dados do IBGE? [S/N]')

x  = [1992, 1995, 1998, 1999, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2011]
fx = [16.44, 14.68, 12.86, 12.3, 11.4, 10.9, 10.6, 10.4, 10.05, 9.41, 9.09, 9.2, 8.9, 7.9]

if dadosIBGE == 'N':
    x  = []
    fx = []
    c = 0
    while True:
        if c > 1:
            encerrar = input('Adicionar mais entradas? [S/N]')
            if encerrar == 'N':
                break
        x.append(float(input('Insirar um Valor de x')))
        fx.append(float(input('Insirar um Valor de f(x)')))
        c+=1
        
contador = len(x)
somaX = somatorio1(x)
somaX2 = somatorio2(x,x)
somaY = somatorio1(fx)
somaXY = somatorio2(x, fx)

# | Contador  ,  SomaX |   | a |   | SomaY  |
# | SomaX     , SomaX2 | * | b | = | SomaXY |

alpha = (-1) * contador / somaX
b =  (alpha * somaXY + somaY) / (alpha * somaX2 + somaX)
a = (somaY - somaX * b) / contador

#print(a)
#print(b)

gx = []
gx = montaGX(gx, x, a, b)
print()
print(f'Equação da reta G(x): {b}x + ({a})')
print(f'Resíduo Quadrático: r2(x) = {residuo2(fx, gx)}')


if dadosIBGE == 'S':
    print()
    print('Prospectiva para o analfabetismo no Brasil')
    print(f'2020: { b*2020 + a :.4}%')

    
matplotlib.pyplot.ioff()
matplotlib.pyplot.plot(x,fx,label='F(x)')
matplotlib.pyplot.plot(x,gx,label= f'G(x): {b:.4}x + ({a:.4})')
if dadosIBGE == 'N':
    matplotlib.pyplot.xlabel('x')
    matplotlib.pyplot.ylabel('y')
else:
    matplotlib.pyplot.xlabel('Ano')
    matplotlib.pyplot.ylabel('Analfabetismo (%)')
matplotlib.pyplot.title('Aproximação de funções - Gustavo R. BEC')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


