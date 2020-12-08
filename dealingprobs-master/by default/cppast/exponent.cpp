#include<stdio.h>
int main()
{
	int a,b,c=0,d;
	printf("\n enter base value");
	scanf("%d",&a);
	printf("\n enter exponential value");
	scanf("%d",&b);
	for(c=0;c<b;c++)
	{
		d=d*a;
	}
	printf("Value=%d",d);
}
