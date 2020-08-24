#include<stdio.h>
int main()
{
	int n[2][2],m[2][2],o[2][2],i,j,k,a,b,c,d;
	printf("\n Enter no of rows and column of Matrix 1: ");
	scanf("%d%d",&a,&b);
	for(i=0;i<a;i++)
	{
		for(j=0;j<b;j++)
		{
			printf("\n Enter a%d%d of 1st matrix",i+1,j+1);
			scanf("%d",&n[i][j]);
		}
	}
	printf("\n Enter no of rows and column of Matrix 2: ");
	scanf("%d%d",&c,&d);
	for(i=0;i<c;i++)
	{
		for(j=0;j<d;j++)
		{
			printf("\n Enter b%d%d of 2nd matrix",i+1,j+1);
			scanf("%d",&m[i][j]);
		}
	}
	printf("Matrix 1:\n");
	for(i=0;i<a;i++)
	{
		for(j=0;j<b;j++)
		{
			printf(" %d",n[i][j]);
		}
		printf("\n");
	}
	printf("Matrix 2:\n");
	for(i=0;i<c;i++)
	{
		for(j=0;j<d;j++)
		{
			printf(" %d",m[i][j]);
		}
		printf("\n");
	}
	printf("Daigonal Matrix:\n");
	for(i=0;i<a;i++)
	{
		for(j=0;j<d;j++)
		{
			o[i][j]=0;
			for(k=0;k<2;k++)
			{o[i][j]+=n[i][k]*m[k][j];
			}
			{printf(" %d",o[i][j]);}
		}
		printf("\n");
	}
	return 0;
}
