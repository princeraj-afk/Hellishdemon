#include<stdio.h>
#include<string.h>
int main()
{
	char nm[30];
	int l=0,i=0,j;
	printf("\n Enter name");
	gets(nm);
	l=strlen(nm);
	for(i=l;i>0;i--)
	{if (nm[i]==' ')
	break;
}
for(j=i+1;j<l;j++)
	{printf("%c",nm[j]);}
	return 0;
}
