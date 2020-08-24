#include<stdio.h>
#include<conio.h>
int main()
{
	int n[5],i,a,b,c,d,e;
	for(i=0;i<5;i++)
	{c=n[0];
	printf("\n Enter numbers");
	scanf("%d",&n[i]);
	 if(n[i]>a)
	 {
	 	a=n[i];
	 }
	 while(b<a)
	 {if(n[i]>b)
	 {
	 	b=n[i];
	 }
	 }
	 while(c<b)
	 {if(n[i]>c)
	 {
	 	c=n[i];
	 }
	 }
	  while(d<c)
	 {if(n[i]>d)
	 {
	 	d=n[i];
	 }
	 }
	  while(e<d)
	 {if(n[i]>e)
	 {
	 	e=n[i];
	 }
	 printf("%d>%d>%d>%d>%d",a,b,c,d,e);
	 }
	  
  }
	return 0;
}
