#include<stdio.h>
int main()
{
	int n[3][4],i,j,rt[3];
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
}1
