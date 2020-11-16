#include<stdio.h>
#include<string.h>
#include<dos.h>
int main()
{
	char nm[30];
	int l,i=0,j=0;
	printf("Enter name:");
	gets(nm);
	l=strlen(nm);
	for(i=0;i<=l;i++)
	{
		for(j=0;j<i;j++)
		{
			delay. sleep(5);
			printf("%c",nm[j]);
		}
		printf("\n");
	}
	return 0;
}
