#include <iostream>
double max(double x[], int n);
//Para os outros Ex, basta ajustar a funcao calc
double calc(double x);
double erro(double x, double y);
double xTil(double x, double y);
double mod(double x);
double fxfa(double x, double y);


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
 

  std::cout << "Valor da raiz: "<<x[iX-1]<< " ± "<<e;
}

double max(double x[], int n){
  double temp=0;
  for(int i=0;i<n;i++){
    if(x[i]>temp){
      temp=x[i];
    }
  }
  return temp;
}

double calc(double x){
  return (x*x+(0.96*x)-2.08);
}

double erro(double x, double y){
  return (y-x)/2;
}

double xTil(double x, double y){
  return (y+x)/2;
}

double mod(double x){
  if(x<0)
    return x*(-1);
  return x;
}

double fxfa(double x, double y){
  double temp = calc(x);
  double temp1 = calc(y);

  return temp*temp1;
}
