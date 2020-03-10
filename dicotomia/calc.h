double max(double x[], int n);
//Para os outros Ex, basta ajustar a funcao calc
double calc(double x);
double erro(double x, double y);
double xTil(double x, double y);
double mod(double x);
double fxfa(double x, double y);


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
