#include<stdio.h>
int main()
{ int a,b,c;
	printf("Enter three numbers");
	scanf("%d%d%d",&a,&b,&c);
	if (a>b&&a>c)
	{
	printf("%d is the greatest of them",a);
	}
	if (b>a&&b>c)
	{
	printf("%d is the greatest of them",b);
	}
	if (c>b&&c>a)
	{
	printf("%d is the greatest of them",c);
	}
	return 0;
}
