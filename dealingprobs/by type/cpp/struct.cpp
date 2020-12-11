#include<iostream>
#include<conio.h>
#include<iomanip>
using namespace std;

typedef struct employee
{
    /* data */
    int eId;
    char favChar;
    float salary;
} ep;

int main(){
    ep prince;
    prince.eId = 420098;
    prince.favChar = 'S';
    prince.salary = 34.324;
    cout<<prince.favChar<<"\n"<<prince.eId<<"\n"<<prince.salary;
    return 0;
}