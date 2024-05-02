#include <math.h>
 
double squareRoot(const double a) {
    double b = sqrt(a);
    if(b != b) { // nan check
        return -1.0;
    }else{
        return sqrt(a);
    }
}
double addition(double a, double b) {
  double total = a + b; 
  return total;
}
int foo (int x) {
  int arr[4] = {1,2,3,4};
  return arr[5];
}
