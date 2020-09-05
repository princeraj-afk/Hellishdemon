#include<iostream>
#include<conio.h>
#include<iomanip>
using namespace std;

class Complex{
    int a;
    int b;

    public:
        void setData(int v1,int v2){
            a = v1;
            b = v2;}
        
        void setdatabysum(Complex o1,Complex o2){
            a = o1.a+o2.a;
            b = o1.b+o2.b;
        }
        void printnum(){
            cout<<"The complex num is "<<a<<"+"<<b<<"i\n";
        }

};

int main(){
    Complex c1,c2,c3;
    c1.setData(1,3);
    c1.printnum();
    c2.setData(2,4);
    c2.printnum();
    c3.setdatabysum(c1,c2);
    c3.printnum();    
    return 0; 
}