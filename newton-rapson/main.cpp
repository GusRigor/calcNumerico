/*
Método Newton Rapson
Feito em função dos exercícios da
segunda aula do curso de calcNumérico
Por: Gustavo G. Rigor
*/
#include <iostream>
#include <math.h>

double f(double x);
double df(double x);
double mod(double x);
double erro(double x, double y);

int main() {
    double precisao = 0.001;
    double x0 = 1.0;
    double Xn[50];
    int n = 0;

    Xn[n++] = x0;
    Xn[n] = Xn[n - 1] - (f(Xn[n - 1]) / df(Xn[n - 1]));

    while (precisao<erro(Xn[n],Xn[n-1]))
    {
        Xn[++n] = Xn[n - 1] - (f(Xn[n - 1]) / df(Xn[n - 1]));
        std::cout << Xn[n]<<"\n";
    }
    
    std::cout << Xn[n];

	return 0;
}

double f(double x) {
    return (x*x*x*x)-2.0;
}

double df(double x) {
    return (x * x * x)*4;
}

double mod(double x) {
    if (x < 0)
        return x * (-1);
    return x;
}
double erro(double x, double y) {
    return mod((y - x) / 2);
}