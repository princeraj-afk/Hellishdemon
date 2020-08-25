#include<stdio.h>
#include<conio.h>
int main()
{int i=79,c=0;
while (i>2)
{printf("\n %d",i-=2);
c++;
if(c==10)
{
	printf("\nPress any key to continue.....");
	getch();
	c=0;
}
}
	return 0;	
}
