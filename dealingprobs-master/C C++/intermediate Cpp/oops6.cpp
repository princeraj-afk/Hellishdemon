#include<iostream>
using namespace std;

class Student{
    protected:
        int rollNo;
    public:
        void setRollno(int a){
            rollNo = a;
        }
        void printRollNo(){
            cout<<"Your roll no is "<<rollNo<<endl;
        }
};
class Test : virtual public Student{
    protected:
        int physics,maths;
    public:
        void setMarks(int a,int b){
            physics = a;
            maths = b;
        }
};
class Sport : virtual public Student{
    protected:
        int physical_edu;
    public:
        void setScore(int a){
            physical_edu = a;
        }
};
class Result :public Test,public Sport{
    public:
        void printResult(){
            cout<<"Your roll no is "<<rollNo<<endl
                <<"Your total marks is "<<physics + maths + physical_edu;
        }
};


int main(){
    Result prince;
    prince.setRollno(3456);
    prince.setMarks(45,56);
    prince.setScore(90);
    prince.printResult();
    return 0;
}