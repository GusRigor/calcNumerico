/*
Método do ponto fixo
Feito em função dos exercícios da
segunda aula do curso de calcNumérico
Por: Gustavo G. Rigor
*/
#include <iostream>
#include <math.h>
double max(double x[], int n);
double fi(double x);
double dfi(double x);


int main() {
	double resultado = 0;

	return 0;
}

double fi(double x) {
    return (2.08 - 0.96 * x) / x;
}

double dfi(double x) {
    return (-2.08 / (x * x));
}

double max(double x[], int n) {
    double temp = 0;
    for (int i = 0; i < n; i++) {
        if (x[i] > temp) {
            temp = x[i];
        }
    }
    return temp;
}