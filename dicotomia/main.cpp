#include <iostream>
#include "calc.h"

int main() {
  int iA=0;
  int iB=0;
  int iX=0;
  double a[50];
  double b[50];
  double x[100];
  double e=0;
  a[iA++] = (-1.8); 
  b[iB++] = (-2.4);
  
  //O q dita a parada do laço é isso, logo,
  //enquanto não for verdade, continua rodando
  //isso = mod(x[iX]-x[iX-1]) < (e*max(x,iX))
  do{
    x[iX++] = xTil(a[iA-1],b[iB-1]);
    e = erro(a[iA-1],b[iB-1]);

    if(0 > fxfa(x[iX-1],a[iA-1])){
      b[iB++] = x[iX-1];
    }else{
      a[iA++] = x[iX-1];
    }


  }while(mod(x[iX-1]-x[iX-2]) > (e*max(x,(iX-1))));
 

  std::cout << "Valor da raiz\nExercício A: "<<x[iX-1]<< " ± "<<e<<"\n";
}
