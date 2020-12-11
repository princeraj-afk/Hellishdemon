#include<stdio.h>
#include<conio.h>
int main()
{
	int n[5],i,c;
	for(i=0;i<5;i++)
	{c=n[0];
	printf("\n Enter numbers");
	scanf("%d",&n[i]);
	 if(n[i]<c)
	 {
	 	c=n[i];
	 }
  }
    printf("lowest=%d",c);
	return 0;
}
