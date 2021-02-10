#Esse é um programa/biblioteca de funções para auxilar na resolução de exercícios de Ondas
#e Eletromagnetismo.
from math import pi, cos, sqrt, atan, e

#Aqui alguns dos valores a serem usados durante a utilização

j=(-1)**(1/2) #Para se referir a números complexos
mi0 = 4*pi*(10**(-7)) #permeabilidade do vácuo
eps0 = 1/(36*pi)*(10**(-9)) #permessividade do vácuo
v0 = c = 1/sqrt(mi0*eps0) #velocidade de propagação da luz no vácuo
n0 = sqrt(mi0*eps0) #impedância característica do vácuo

def frequencia_linear_para_angular(f):
    return 2*pi*f

def retangular_para_polar_amplitude(z):
    return sqrt((z.real**2)+(z.imag**2)) 

def retangular_para_polar_fase(z):
    return atan(z.imag/z.real)

#Para meios sem perda
def impedancia_sem_perda(miR, epsR):
    return n0*sqrt(miR/epsR)

def velocidade_sem_perda(miR, epsR):
    return v0/sqrt(miR/epsR)

def comprimento_de_onda_sem_perda(miR, epsR, f):
    return velocidade_sem_perda(miR, epsR)/f

    #Beta é constante de fase
def beta_sem_perda(miR, epsR, f):
    return frequencia_linear_para_angular(f)*(sqrt(miR/epsR)/v0)

def comprimento_de_onda_sem_perda_beta(beta):
    return (2*pi)/beta

#Para meios com perda, aparecerá um atenuação.

#Condutividade elétrica sigma
def constante_de_propagacao(sigma, miR, epsR, f):
    return sqrt((j*miR*mi0*frequencia_linear_para_angular(f))*(sigma+j*epsR*eps0*frequencia_linear_para_angular(f)))

#Constante de atenuação alpha
def alpha_constante_de_atenuacao(sigma, miR, epsR, f):
    return constante_de_propagacao(sigma, miR, epsR, f).real

#Constante de fase
def beta_constante_de_fase(sigma, miR, epsR, f):
    return constante_de_propagacao(sigma, miR, epsR, f).imag

def impedancia_com_perda(sigma, miR, epsR, f):
    return sqrt((j*miR*mi0*frequencia_linear_para_angular(f))/(sigma+j*epsR*eps0*frequencia_linear_para_angular(f)))

def velocidade_com_perda(sigma, miR, epsR, f):
    return frequencia_linear_para_angular(f)/beta_constante_de_fase(sigma, miR, epsR, f)

def ccomprimento_de_onda_com_perda(sigma, miR, epsR, f):
    return (2*pi)/beta_constante_de_fase(sigma, miR, epsR, f)

def profundidade_pelicular(sigma, miR, epsR, f):
    return 1/alpha_constante_de_atenuacao(sigma, miR, epsR, f)

def potencia_ondas(tensao, distancia, area, sigma, miR, epsR, f):
    n = retangular_para_polar_amplitude(impedancia_com_perda(sigma, miR, epsR, f))
    n_fase = retangular_para_polar_fase(impedancia_com_perda(sigma, miR, epsR, f))
    alpha = alpha_constante_de_atenuacao(sigma, miR, epsR, f)
    return area*cos(n_fase)*(e**(-2*alpha*distancia))*(tensao**2)/n

#Linha de transmição
#onde a indutancia e capacitancia da linha são l e c, repectivamente
def impedancia_linha_de_transmicao(l,c):
    return sqrt(l/c)

#onde a impedancia do meio 1 e 2 são n1 e n2, repectivamente
def coeficiente_refracao(n1, n2):
    return(n2-n1)/(n2+n1)

def coeficiente_transmicao(n1, n2):
    return(2*n2)/(n2+n1)

def densidade_potencia(coeficiente, tensao, impedancia):
    return (coeficiente**2)*(tensao**2)/(2*impedancia)


print(constante_de_propagacao(2, 1, 2.25, 15*(10**9)))
