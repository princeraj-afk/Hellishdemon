#include<iostream>
#include<conio.h>
#include<iomanip>
using namespace std;

//union takes the data tye of max sixe and ignore all the rest
typedef union dexter
{
    int eId;
    char favChar;
    float salary;
} dx;

int main(){
    dx prince;
    prince.eId = 420098;
    cout<<prince.favChar<<"\n"<<prince.eId<<"\n"<<prince.salary;

    prince.favChar = 'S';
    cout<<prince.favChar<<"\n"<<prince.eId<<"\n"<<prince.salary;

    prince.salary = 34.324;
    cout<<prince.favChar<<"\n"<<prince.eId<<"\n"<<prince.salary;
    return 0;
}