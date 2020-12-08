#include<stdio.h>
int main()
{
	int a=2,b,c,d;
	b=++a;
	c=b++;
	d=a--;
	printf("A=%d B=%d C=%d D=%d",a,b,c,d);
}
