#include <iostream>
#include <string>
using namespace std; 

// Part 2
int noNameFunc2(int c, int s){
  if( c == 1 ){
    return s;
  }else {
    return noNameFunc2(c-1, s * c);
  }
}


int noNameFunc1(int n) {
  if (n == 0) {
    return 1;
  }
 
  return noNameFunc2(n,1);
}



int main() {
  //Part 1
  // int n = 0;
  // while(1){
  //   n = n+2;
  //   if(n%3 == 0) {
  //     printf("***%d", n);
  //     break;
  //   }
  //   if (n% 5 == 0) {
  //     printf("###%d", n);
  //     continue;
  //   }
  //   n = n + 1;
  // }

  // Part 2
  int ans = noNameFunc1(9);
  cout << ans;
  
  return 0;

}

