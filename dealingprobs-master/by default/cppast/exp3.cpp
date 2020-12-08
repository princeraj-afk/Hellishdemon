#include<stdio.h>
int exp(int,int);
int main()
{
	int a,b,e;
	printf("Enter base and exp value");
	scanf("%d%d",&a,&b);
	e=exp(a,b);
	printf("Exponential of number is %d",e);
}
int exp(int p,int q)
{if ( q<1)
  {
  	return 1;
  }
  else
  {
return (p*exp(p,q-1));
}
}
