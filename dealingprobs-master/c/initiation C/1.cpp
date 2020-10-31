#include<stdio.h>
#include<string.h>
int main()
{
	char nm[30];
	int l,i=0,j=0,k;
	printf("\n Enter name");
	gets(nm);
	l=strlen(nm);
	printf("%c.",nm[0]);
	for(i=l-1;i>0;i--)
	{if (nm[i]==' ')
	{break;}}
	for(j=0;j<i;j++)
	{if (nm[j]==' ')
	printf("%c.",nm[j+1]);
	}
	for(k=i+1;k<l;k++)
	{
	printf("%c",nm[k]);}
	return 0;
}
