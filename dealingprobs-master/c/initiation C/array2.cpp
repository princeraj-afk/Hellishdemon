#include<stdio.h>
#include<conio.h>
int main()
{
	int n[3][4],i,j;
	for(i=0;i<3;i++)
	{for(j=0;j<4;j++)
	{printf("\nEnter numbers");
	scanf("%d",&n[i][j]);
	printf("%d",n[i][j]);
	}	
}printf("\n");
	for(i=0;i<3;i++)
	{for(j=0;j<4;j++)
	{printf(" %d",n[i][j]);}
	printf("\n");
	}
return 0;
}
