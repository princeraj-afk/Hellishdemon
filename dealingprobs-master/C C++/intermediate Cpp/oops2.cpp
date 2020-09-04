#include<iostream>
#include<conio.h>
#include<iomanip>
using namespace std;

class option()
{
    string s;
    void func3(void);
    void func4(void);

public:
    void func1(void);
    void func2(void);

};

void option :: func1(void)
{    cout<<"You are in func1";}
void option :: func2(void)
{    cout<<"You are in func2";}
void option :: func3(void)
{    cout<<"You are in func3";}
void option :: func4(void)
{    cout<<"You are in func4";}


int main(){
    
    return 0;
}