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
double mod(double x);
//Para este programa para novas funcoes será preciso alterar as funcoes fi e dfi

int main() {
    double x0 = 1.2;
    double aux = 0;
    int n = 0;
    double xN[50];
    int nfi = 0;
    double dfi0[50];
    double k = 0;

    xN[n] = x0;
    aux = fi(xN[n]);
    dfi0[nfi++] = dfi(xN[n++]);

    std::cout << "Valor inicial: \n";
    std::cout << "Xn: " << xN[n - 1] <<" Fi(Xn): " << aux <<" Fi'(Xn): " << dfi0[nfi - 1] << "\n\n";

    do {

        xN[n] = aux;
        aux = fi(xN[n]);
        dfi0[nfi] = dfi(xN[n++]);
        std::cout << "Xn " << xN[n - 1] <<" Fi(Xn): "<< aux <<" Fi'(Xn): " << dfi0[nfi] << "\n";

        k = max(dfi0, nfi);
        nfi++;

    } while (aux - xN[n - 1] >= (k / (1 - k)) * mod(xN[n - 1] - xN[n - 2]));


    std::cout << "Resultado:\n";
    std::cout << "Xn - " << xN[n - 1] << " Fi(Xn) - " << aux << "\n";

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
double mod(double x) {
    if (x < 0)
        return x * (-1);
    return x;
}