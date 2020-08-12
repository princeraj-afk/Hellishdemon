#include<stdio.h>
#include<conio.h>
int main()
{
	int n[3][4],i,j,rt[3],ct[4];
	for(i=0;i<3;i++)
	{
		rt[i]=0;
		for(j=0;j<4;j++)
		{
			printf("\nEnter No");
			scanf("%d",&n[i][j]);
			rt[i]+=n[i][j];
		}
	}
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<4;j++)
		{
			printf("%d ",n[i][j]);
		}
		printf("\t%d",rt[i]);
		printf("\n");
	}
	for(j=0;j<4;j++)
	{
			ct[j]=0;
			for(i=0;i<3;i++)
	{
			ct[j]+=n[i][j];
			
		}
		printf("%d ",ct[j]);
	}
	return 0;
}
