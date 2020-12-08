#include<stdio.h>
void max(int a,int b)
{
	int c=0;
	c=a>b?a:b;
	printf("greater:%d",c);
}
int main()
{
	int p,q;
	printf("\nEnter two Numbers");
	scanf("%d%d",&p,&q);
	max(p,q);
}
