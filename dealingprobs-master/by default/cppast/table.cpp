#include<stdio.h>
int main()
{
	int a=2,p=1;
	while (a<6)
	{
	while (p<11)
	{printf("\n %d*%d=%d",a,p,a*p);
	p++;
	}
	p=1;
	a++;
}
return 0;
}
