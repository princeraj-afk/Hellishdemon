#include<stdio.h>
int main()
{
	int n,x=0,d=0,r=0,c=0,v=0;
	float mp=0.;
	printf("\n Enter number");
	scanf("%d",&n);
	x=n;
	while(x!=0)
	{x/=10;
	v++;
	}
	mp=(float)(v+1)/2;
	while(n!=0)
	{d=n%10;
	c++;
	if (c!=mp)
	{ r=r*10+d;
	}
	n/=10;
}
printf("Reverse is %d",r);
return 0;
}
