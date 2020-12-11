#include<stdio.h>
#include<string.h>
int main()
{
	char nm[30];
	int l=0,i;
	printf("\n Enter name");
	gets(nm);
	l=strlen(nm);
	for(i=0;i<l;i++)
	{if (nm[i]==' ')
	{break;
	}
	else
	{printf("%c",nm[i]);
	}
	}
	return 0;
}
