#include<stdio.h>
int main()
{
	int n[5],i,a,c=0;
	for (i=0;i<5;i++)
	{
		printf("\n Enter some numbers");
		scanf("%d",&n[i]);
	}
	printf("\n Enter the number");
	scanf("%d",&a);
	for(i=0;i<5;i++)
		{
			if(a==n[i])
			{printf("\n Found %d",a);
			c++;}
			else
			continue;
		}
	if(c==0)
	{printf("\n Not found");}
	return 0;
}
