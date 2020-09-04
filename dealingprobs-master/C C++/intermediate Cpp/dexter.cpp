#include<iostream>
#include<conio.h>
#include<iomanip>
using namespace std;

// long double factorial(int n){
//     if (n<=1){
//         return 1;
//     }
//     return n *factorial(n-1);
// }

int fibonacci(int n){
    if (n<=2){
        return 1;
    }
    return fibonacci(n-1)+fibonacci(n-2);
}

int main(){
    int a;
    cout<<"Enter the number"<<endl;
    cin>>a;
    cout<<fibonacci(a);      
    return 0; 
} 