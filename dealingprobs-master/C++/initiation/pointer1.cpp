#include<stdio.h>
#include<conio.h>
int main()
{
	int n[5],i,*p;
	for(i=0;i<5;i++)
	{
		printf("\nEnter number");
		scanf("%d",&n[i]);
	}
	p=n;
	for(i=0;i<5;i++)
	{if(*(p+i)%2==0)
	{
		printf("%d",*(p+i));
	}
	else
	{
		continue;
	}
}
	return 0;
}

