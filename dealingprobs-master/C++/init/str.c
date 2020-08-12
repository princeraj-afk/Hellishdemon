#include<stdio.h>
#include<string.h>
int main()
{
	char a[10],b[10],c[10];
	printf("\nEnter 1st name");
	gets(a);
	printf("\nEnter nd name");
	gets(b);
	if(strcmp(a,b)>0)
	{
	 strcpy(c,a);	
	 strcpy(a,b);
	 strcpy(b,c);
	}
		printf("a=%s",a);
		printf("b=%s",b);
}
