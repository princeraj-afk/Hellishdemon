#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
    int age;
    cout<<"tell me your age"<<endl;
    cin>>age;
    // if (age<18){
    //     cout<<"you cannot come to the party";
    // }
    // else if(age==18){
    //     cout<<"You are a kiddo even now!";
    // }
    // else{
    //     cout<<"you are welcomed to the party";
    // } 

    switch (age)
    {
    case 18:
        /* code */
        break;
    
    default:
        break;
    }
    return 0;
}