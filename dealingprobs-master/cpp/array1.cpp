#include<stdio.h>
#include<conio.h>
int main()
{
	int n[5],i;
	for(i=0;i<5;i++)
	{printf("\n Enter numbers");
	scanf("%d",&n[i]);}
	for(i=0;i<5;i++)
	if (n[i]%2==0)
	{printf("%d",n[i]);
	}
	else
	continue;
	return 0;
}
