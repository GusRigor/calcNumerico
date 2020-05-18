import matplotlib.pyplot

def condInicial(x):
    return x*(x-1)

def tNmais1(t, i):
    if i == 10:
        return t[i] + gama*(t[i-1] - 2*t[i] + 0)
    return t[i] + gama*(t[i-1] - 2*t[i] + t[i+1])

def vetTmais1(t1, t0):
    c = 0
    while True:
        if c > 10:
            break
        #print(c)
        t1.append(tNmais1(t0, c))
        #print(c)
        c += 1
            

alpha = 0.1
varT  = 1
varX  = 10
t0    = 0
tIM   = 0

gama = alpha*varT/varX**2
#print(gama)

x = 0
i = 0

T  = [0,1,2,3,4,5,6,7,8,9,10]
T0 = []

while True:
    if x > 100:
        x = 0
        break
    T0.append(condInicial(x))
    x += varX

print(T0)

T1 = []
vetTmais1(T1, T0)
print(T1)

T2 = []
vetTmais1(T2, T1)
print(T2)

T3 = []
vetTmais1(T3, T2)
print(T3)

T4 = []
vetTmais1(T4, T3)
print(T4)

T5 = []
vetTmais1(T5, T4)
print(T5)

T6 = []
vetTmais1(T6, T5)
print(T6)

T7 = []
vetTmais1(T7, T6)
print(T7)

T8 = []
vetTmais1(T8, T7)
print(T8)

T9 = []
vetTmais1(T9, T8)
print(T9)

T10= []
vetTmais1(T10, T9)
print(T10)

matplotlib.pyplot.plot(T,T0,label='T0(t)')
matplotlib.pyplot.plot(T,T1,label='T1(t)')
matplotlib.pyplot.plot(T,T2,label='T2(t)')
matplotlib.pyplot.plot(T,T3,label='T3(t)')
matplotlib.pyplot.plot(T,T4,label='T4(t)')
matplotlib.pyplot.plot(T,T5,label='T5(t)')
matplotlib.pyplot.plot(T,T6,label='T6(t)')
matplotlib.pyplot.plot(T,T7,label='T7(t)')
matplotlib.pyplot.plot(T,T8,label='T8(t)')
matplotlib.pyplot.plot(T,T9,label='T9(t)')
matplotlib.pyplot.plot(T,T10,label='T10(t)')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (T0(t) e T1(t) e T2(t) e T3(t) e T4(t) e T5(t) e T6(t) e T7(t) e T8(t) e T9(t) e T10(t))')
matplotlib.pyplot.title('Exercício EDP Calor graph - Gustavo R. BEC')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
