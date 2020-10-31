#include<stdio.h>
#include<conio.h>
int main()
{
	int n[5],i,j,iv=0;
	for (i=0;i<5;i++)
	{printf("\n Enter numbers");
	scanf("%d",&n[i]);
	}
	for (i=0;i<5;i++)
	{
		for (j=i+1;j<5;j++)
		{
			if(n[i]>n[j])
			{
				iv=n[i];
				n[i]=n[j];
				n[j]=iv;
			}
		}
	}
	for (i=0;i<5;i++)
	{
		printf("%d ",n[i]);
	}
	return 0;
}
