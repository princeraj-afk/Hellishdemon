#include<stdio.h>
int exp(int a,int b)
{	int c=0,d=1;
for(c=0;c<b;c++)
	{
		d=d*a;
	}
	return d;
}
int main()
{
	int p,q;
	printf("\n enter base value and exponential value respectively");
	scanf("%d%d",&p,&q);
	printf("\n exponent=%d",exp(p,q));
}

