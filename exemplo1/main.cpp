#define PI 3.14159265

#include <iostream>
#include <math.h>

unsigned long long fatorial( int n )
{
    unsigned long long f = 1;
    for( ; n > 0; f *= n-- );
    return f;
}

double convRad(double x){
  return x*(PI/180);
}
double cosseno(double x){
    double i = 1 - (pow(x,2)/fatorial(2));
    return i;
}

double cosseno10(double x){
  	int contador;
	double resultado;
	resultado = 0;
		while(x>(2*PI)){
		x=x-2*PI;
		}
	for(contador = 0; contador < 10;contador++){
		resultado = resultado + pow(-1, contador) * pow(x, 2*contador) / fatorial(2*contador);
	}

	return resultado;
}


double seno(double x){
    double i = x - (pow(x,3)/fatorial(3));
    return i;
}

double seno10(double x){
  	int contador;
	double resultado;
	resultado = 0;
		while(x>(2*PI)){
		x=x-2*PI;
		}
	for(contador = 0; contador < 10;contador++){
		resultado = resultado + pow(-1, contador) * pow(x, 2*contador + 1) / fatorial(2*contador + 1);
	}

	return resultado;
}

double expo(double x){
    
  return 1 + (pow(x,1))/fatorial(1);
}
double expo10(double x){
  double j = 0;
  for(int i=0; i<=10; i++){
    j += (pow(x,i))/fatorial(i);
  }
  return j;
}
double erroRelativo(double esperado, double obtido){
  return(((obtido-esperado)/esperado)*100);
}

int main() {
  int x = 2;
  x = pow(2,2);
  double v = 2.71828182846;
  double y = fatorial(4);
  double y1 = 0;
  y = expo(1);
  y1 = expo10(1);

  std::cout<<"Exponencial \n";
  std::cout<< y <<"\n"<<y1<<"\n";
  std::cout<<"Erro relativo: "<<erroRelativo(v,y)<<"\n";
  std::cout<<"Erro relativo de 10: "<<erroRelativo(v,y1);

  y = seno(convRad(30));
  y1 = seno10(convRad(30));
  v = 0.500000;

  std::cout<<"\n\nSeno de 30 \n";
  std::cout<< y <<"\n"<<y1<<"\n";
  std::cout<<"Erro relativo: "<<erroRelativo(v,y)<<"\n";
  std::cout<<"Erro relativo de 10: "<<erroRelativo(v,y1);

  y = cosseno(convRad(60));
  y1 = cosseno10(convRad(60));
  v = 0.500000;


  std::cout<<"\n\nCosseno de 60 \n";
  std::cout<< y <<"\n"<<y1<<"\n";
  std::cout<<"Erro relativo: "<<erroRelativo(v,y)<<"\n";
  std::cout<<"Erro relativo de 10: "<<erroRelativo(v,y1);
}
