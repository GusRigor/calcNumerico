#define PI 3.14159265359
#include<math.h>
#include <stdio.h>

void arredondado(double x);
void truncado(double x);

void arredondado(double x){
  x += 0.000005;
  printf("%.5lf \n\n", x);

}
void truncado(double x){
  printf("   %.5lf \n", x);

}

void imprime(double x){
  printf("Valor truncado: "); truncado(x);
  printf("Valor arredondado: "); arredondado(x);
}

int main(){

	double valor[5] = {sqrt(2), (1.0/9.0), PI, (1.0/7.0), (100.0/7.0)};
  
  for(int i=0;i<5;i++){
    printf("Exercício %d): \n",i+1);
    imprime(valor[i]);
    
  }
	return 0;
}
