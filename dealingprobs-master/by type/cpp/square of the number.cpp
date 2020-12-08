#include<stdio.h>
#include<conio.h>
int main()
{
	int a,n,c=0;
	printf("\n Enter the number");
	scanf("%d",&n);
	while(n!=0)
	{
		printf("the square of the number is %d",n*n);
	c++;
	if (c==1)

	{
		printf("press any key to continue");
		getch ();
		c=0;
	}
}
	return 0;
}
