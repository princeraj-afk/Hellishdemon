#include<stdio.h>
#include<conio.h>
int main()
{
	int i,j,c;
	for(i=1;i<=5;i++)
{for(j=1;j<=i;j++)
{printf("%d",i);}
for (c=0;c<i;c+=4)
{printf("\n");}
}
return 0;
}
