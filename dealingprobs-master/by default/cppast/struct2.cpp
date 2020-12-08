#include<stdio.h>
#include<conio.h>
struct student
{
int rollno;
char name[25];
int totalmark;
};
int main()
{
struct student stud[6];
int i;
    for(i=0;i<6;i++)
{
printf("Enter details of %d-th student\n",i+1);
printf("Name:\n");
scanf("%s",&stud[i].name);
printf("Roll number:\n");
scanf("%d",&stud[i].rollno);
printf("Total mark:\n");
scanf("%d",&stud[i].totalmark);
}
printf("STUDENTS DETAILS:\n");
printf("S.No.   Roll \tName \tMarks \n\n");
for(i=0;i<6;i++)
{
	printf("%d",i+1);
printf("%d",stud[i].rollno);
printf("%s",stud[i].name);
printf("%d",stud[i].totalmark);
printf("\n");
}
getch();
return 0;
}
