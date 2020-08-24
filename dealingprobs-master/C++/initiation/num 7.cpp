#include<stdio.h>
int main()
{
	int a,n,c=0,x,d=0,r=0;
	printf("enter any number");
	scanf("%d",&n);
	x=n;
	while (n!=0)
	{ n/=10;
	c++;
	}
	printf("%d",c);
	a=c%2;
	if (a=0)
	while(x!=0)
	{d=x%10;
	r=r*10+d;
	x/=10;
	}
	printf("\n%d",r);
	return 0;
}
