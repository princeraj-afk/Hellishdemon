#include<stdio.h>
#include<string.h>
int main()
{
	char nm[30];
	int l,i,j,k=0;
	printf("\n Enter name");
	gets(nm);
	l=strlen(nm);
	for(i=0;i<l;i++)
	{if (nm[i]==' ')
	{break;
	}
}
for (j=l-1;j>0;j--)
	{if (nm[j]==' ')
	{break;}}
	for (k=i+1;k<j;k++)
	{printf("%c",nm[k]);
	}
	return 0;
}
