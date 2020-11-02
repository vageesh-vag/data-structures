#include<iostream>
using namespace std;
class node
{
    public:
	int data;
	class node *next;
}
*front=NULL;
class queue
{
	public:
	void insert()
	{
	    int x;
		cout<<"enter x\n";
		cin>>x;
		node *temp=new node;
		temp->data=x;
		temp->next=NULL;
		if(front==NULL)
		{
			cout<<"queue is empty\n";
			front=temp;
		}
		else
		{
			temp->next=front;
			front=temp;
		}
	}
	void display()
	{
		node *temp1=new node;
		temp1=front;
		while(temp1->next!=NULL)
		{
			cout<<temp1->data<<"->";
			temp1=temp1->next;
		}
		cout<<temp1->data<<"\n";
	}
	void largest()
	{
		node *temp1=new node;
		node *temp2=new node;
		temp1=front;
		temp2=front;
		int largest=temp1->data;
		while(temp1->next!=NULL)
		{
			temp1=temp1->next;
			temp2=temp1;
			if(temp2->data>temp1->data)
			largest=temp2->data;
		}
		cout<<"largest is "<<largest;
	}
};
main()
{
	int choice;
	queue q1;
	while(1)
	{
		cout<<"1.insertion\n2.display\n3.largest\n";
		cout<<"enter choice\n";
		cin>>choice;
		switch(choice)
		{
			case 1:
				q1.insert();
				break;
			case 2:
				q1.display();
				break;
			case 3:
				q1.largest();
				break;
		}
	}
}
