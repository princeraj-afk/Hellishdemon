#include<stdio.h>
#include<malloc.h>
int main()
{
	int *p,i,a,c=0,ch;
	printf("\nEnter Number of elements");
    scanf("%d",&ch);
    p=(int *)malloc(ch*sizeof(int));
    for (i=0;i<ch;i++)
	{
		printf("\n Enter some numbers");
		scanf("%d",(p+i));
	}
	printf("\n Enter the number");
	scanf("%d",&a);
	for(i=0;i<5;i++)
		{
			if(a==*(p+i))
			{printf("\n Found %d",a);
			c++;}
			else
			continue;
		}
	if(c==0)
	{printf("\n Not found");}
	return 0;
}
