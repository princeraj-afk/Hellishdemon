#include<stdio.h>
#include<conio.h>
struct book
{
	char nm[30],anm[40];
	int price;
};
int main()
{
	struct book bk[6];
	int i;
	for(i=0;i<6;i++)
	{
		printf("enter details of %d-th book \n",i+1);
		printf("Name of book:\n");
		scanf("%s",bk[i].nm);
		printf("Name of Author:\n");
		scanf("%s",bk[i].anm);
		printf("price of the book:\n");
		scanf("%d",bk[i].price);
	}
	printf("BOOK DETAILS:\n");
	for(i=0;i<6;i++)
	{
		printf("book name:%s\n",bk[i].nm);
		printf("author name:%s\n",bk[i].anm);
		printf("price of book:%d",bk[i].price);
	}
	return 0;
}
