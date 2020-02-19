#include <iostream>
#include <math.h>
unsigned long long fatorial( int n )
{
    unsigned long long f = 1;
    for( ; n > 0; f *= n-- );
    return f;
}

  double seno(double x){
    double i = ((pow(-1,1))/fatorial((2*1)+1))*(pow(x,((2*1+1))));
    return i;
  }

  double seno10(double x){
    double i;
    for(int j=0; j<10;j++)
      i += ((pow(-1,i))/fatorial((2*i)+1))*(pow(x,((2*i+1))));
    return i;
  }
  double expo(double x){
    
    return 1 + (pow(x,1))/fatorial(1);
  }
  double expo10(double x){
    double j = 0;
    for(int i=0; i<10; i++){
      j += (pow(x,i))/fatorial(i);
    }
    return j;
  }

int main() {
  int x = 2;
  x = pow(2,2);
  double y = fatorial(4);
  double y1 = seno10((3.14159265359)/6);
  y = expo(1);
  y1 = expo10(1);
  std::cout<< y <<"\n"<<y1;
}
