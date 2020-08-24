#include<stdio.h>
int max(int a,int b)
{
 if(a>b)
  {
  	return a;
	  }	
	  else
	  {
	  	return b;
	  }
}
int main()
{
	int p,q;
	printf("\nEnter two Numbers");
	scanf("%d%d",&p,&q);
	printf("\nmax=%d",max(p,q));
}
