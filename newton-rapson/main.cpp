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