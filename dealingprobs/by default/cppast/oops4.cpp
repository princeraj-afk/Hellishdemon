#include <iostream>
#include <conio.h>
#include <iomanip>
using namespace std;

class Employee
{
    int id;

public:
    float salary;
    Employee(int uid)
    {
        id = uid;
        salary = 25000.0;
    }
};

class Programmer : Employee
{
public:
    int Language = 9;

}

int
main()
{
    Employee prince(1);
    cout << prince.salary;
    return 0;
}