#include<stdio.h>
int main()
{
	int j=5,c=1;
	while(c<=5)
	{
		while(j>=c)
		{
			printf("%d",j);
			j--;
		}
		c++;
		j=5;
		printf("\n");
}
}
