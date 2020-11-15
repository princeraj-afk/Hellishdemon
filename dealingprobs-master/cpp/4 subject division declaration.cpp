#include<stdio.h>
int main()
{ int a,b,c,d;
	printf("enter four subject marks");
	scanf("%d%d%d%d",&a,&b,&c,&d);
	if ((a+b+c+d)/4>=60)
	{
		printf("1st Division");
	}
	else if ((a+b+c+d)/4>=45 && (a+b+c+d)/4<60)
	{
		printf("2nd Division");
	}
	else if ((a+b+c+d)/4>=30 && (a+b+c+d)/4<45)
	{
		printf("3rd Division");
	}
	else
	{
		printf("Fail");
	}
	printf("\n %d is the total mark",a+b+c+d);
	printf("\n %d is the average mark",(a+b+c+d)/4);
	return 0;
}
