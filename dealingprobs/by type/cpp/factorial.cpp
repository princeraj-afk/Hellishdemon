#include<stdio.h>
int main()
{
	int n,i,b=1;
	printf("\n Enter numbers");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		{
			b=b*i;
		}
	printf("%d",b);
	return 0;
}
