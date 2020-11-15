#include<stdio.h>
#include<conio.h>
int main()
{
	int n[3][4],i,j,s[3];
	for(i=0;i<3;i++)
	{s[i]=0;
	for(j=0;j<4;j++)
	{printf("\nEnter numbers");
	scanf("%d",&n[i][j]);
	s[i]+=n[i][j];
	}	
}
{for(i=0;i<3;i++)
{for(j=0;j<4;j++)
{printf("%d",n[i][j]);
}
}
printf(" %d",s[i]);
printf("\n");
}
return 0;
}

