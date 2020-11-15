#include <iostream>
using namespace std;

class Shop
{
    int id;
    float price;

public:
    void setData(int id)
    {
        this->id = id;
    }
    void getData()
    {
        cout << "\nThe value of id is " << id << ".\n";
    };
};
int main()
{
    Shop prince;
    prince.setData(34);
    prince.getData();
    return 0;
}