#include<stdio.h>
#include<stdlib.h>
typedef struct ll
{
	int data;
	struct ll *link;
}node;
node *FIRST=NULL;
node *NEW=NULL;
node *TEMP=NULL;
void insertF()
{
		int x;
		NEW=(node *)malloc(sizeof(node));
		printf("Enter Data: ");
		scanf("%d",&x);
		NEW->data=x;
		if(FIRST==NULL)
		{
			NEW->link=NULL;
		}
		else
		{
			NEW->link=FIRST;
		}
		FIRST=NEW;
}
void insertE()
{
	int y;
	NEW=(node *)malloc(sizeof(node));
	printf("Enter Data: ");
	scanf("%d",&y);
	NEW->data=y;
	TEMP=FIRST;
	while(TEMP->link!=NULL)
	{
		TEMP=TEMP->link;
	}
	TEMP->link=NEW;
	NEW->link=NULL;
}
void insertM()
{
	int pl,x,count=0;
	NEW=(node *)malloc(sizeof(node));
	printf("Enter Place: ");
	scanf("%d",&pl);
	printf("Enter data: ");
	scanf("%d",&x);
	TEMP=FIRST;
	while(count!=pl-2)
	{
		TEMP=TEMP->link;
		count++;		
	}
	NEW->data=x;
	NEW->link=TEMP->link;
	TEMP->link=NEW;
}
void deldata()
{
	int x;
	node *PRED=NULL;
	if(FIRST==NULL)
	{
		printf("Linked List is EMPTY!!!");
	}
	else
	{
		printf("Enter the value to delete: ");
		scanf("%d",&x);
		TEMP=FIRST;
		while(TEMP->data!=x&&TEMP->link==NULL)
		{
			PRED=TEMP;
			TEMP=TEMP->link;
		}
		TEMP=TEMP->link;
		PRED->link=TEMP;
	}
}
void dis()
{
	TEMP=FIRST;
	printf("Linked List: \n");
	while(TEMP!=NULL)
	{
		if(TEMP->link!=NULL)
		printf("%d -> ",TEMP->data);
		else
		printf("%d -> NULL\n",TEMP->data);
		TEMP=TEMP->link;
		
	}
}
void main()
{
	int ch;
	g:
	printf("Enter a Choice: ");
	scanf("%d",&ch);
	switch(ch)
	{
		case(1):
		{
			insertF();
			break;
		}
		case(4):
		{
			dis();
			break;
		}
		case(2):
		{
			insertE();
			break;
		}
		case(3):
		{
			insertM();
			break;
		}
		case(5):
		{
			exit(0);
		}
	}
	goto g;
}
