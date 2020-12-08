#include <iostream>
#include <conio.h>
#include <cmath>
using namespace std;

class SimpleCalculator
{
    int a, b;

public:
    void setnums()
    {
        cout << "Enter the numbers";
        cin >> a >> b;
    }
    void performfunctions()
    {
        cout << "a+b is " << a + b << endl;
        cout << "a-b is " << a - b << endl;
        cout << "a*b is " << a * b << endl;
        cout << "a/b is " << a / b << endl;
    }
};

class ScientificCalci
{
    int a, b;

public:
    void setnums()
    {
        cout << "Enter the numbers";
        cin >> a >> b;
    }
    void prop()
    {
        cout << "cos(a) is" << cos(a) << endl;
        cout << "sin(a) is" << sin(a) << endl;
        cout << "exp(a) is" << exp(a) << endl;
        cout << "tan(a) is" << tan(a) << endl;
    }
};


class Hybridcalci : virtual public SimpleCalculator,public scientific{
      
}





int main()
{
    SimpleCalculator p;
    p.setnums();
    p.performfunctions();

    ScientificCalci q;
    q.setnums();
    q.prop();
    return 0;
}