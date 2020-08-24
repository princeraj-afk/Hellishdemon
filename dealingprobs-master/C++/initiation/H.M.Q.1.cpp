#include<stdio.h>
#include<string.h>
int main()
{
	char nm[30];
	int i=0,l=0,r=0,q=0;
	printf("\n Enter name");
	gets(nm);
	l=strlen(nm);
	printf("Total length with space=%d",l);
	for (i=0;i<l;i++)
	{if (nm[i]==' ')
	{r++;} 
	else if (nm[i]=='a'|| nm[i]=='e'|| nm[i]=='i'|| nm[i]=='o'|| nm[i]=='u')	
	{
		q++;
	}
	}
	printf("\nTotal length without space=%d",l-r);
	printf("\nTotal vowels=%d",q);
	printf("\nTotal consonants=%d",l-(r+q));
	return 0;
	}
