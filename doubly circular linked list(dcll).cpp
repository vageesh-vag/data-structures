#include<iostream>
#include<cstdlib>
using namespace std;
class node
{
	public:
	int data;
	class node *next;
	class node *previous;
}
*head=NULL,*last=NULL;
class dcll
{
	public:
	void insertf()
	{
		int x;
		if(head==NULL)
		{
			node *temp=new node;
			cout<<"list is empty\n";
			cout<<"enter x\n";
			cin>>x;
			temp->data=x;
			temp->next=NULL;
			temp->previous=NULL;
			head=temp;
			last=temp;
		}
		else
		{
			node *temp=new node;
			cout<<"enter x\n";
			cin>>x;
			temp->data=x;
			temp->next=NULL;
			temp->previous=NULL;
			temp->next=head;
			head->previous=temp;
			last->next=temp;
			temp->previous=last;
			head=temp;
			 
		}
	}
	void inserte()
	{
		int x;
		cout<<"enter x\n";
		cin>>x;
		if(head==NULL)
		{
			node *temp=new node;
			cout<<"list is empty\n";
			temp->data=x;
			temp->previous=NULL;
			temp->next=NULL;
			head=temp;
			last=temp;
		}
		else
		{
			node *temp=new node;
			temp->data=x;
			temp->previous=NULL;
			temp->next=NULL;
			last->next=temp;
			temp->previous=last;
			temp->next=head;
			head->previous=temp;
			last=temp;
		}
	}
	void insertn()
	{
		int x,i,pos;
		cout<<"enter x\n";
		cin>>x;
		if(head==NULL)
		{
			node *temp=new node;
			cout<<"list is empty\n";
			temp->data=x;
			temp->next=NULL;
			temp->previous=NULL;
			head=temp;
		}
		else
		{
			node *temp=new node;
			i=1;
			cout<<"enter position to enter\n";
			cin>>pos;
			temp->data=x;
			temp->next=NULL;
			temp->previous=NULL;
			node *temp1=new node;
			node *nbl=new node;
			temp1=head;
			nbl=head;
			while(i<pos)
			{
				nbl=temp1;
				temp1=temp1->next;
				i++;
			}
			nbl->next=temp;
			temp->previous=nbl;
			temp->next=temp1;
			temp1->previous=temp;
			}
	}
	void deletef()
	{
		if(head==NULL)
		{
			cout<<"list is empty\n";
		}
		else
		{
			cout<<head->data<<"is deleted\n";
			head=head->next;
			head->previous=last;
			last->next=head;
			
		}
	}
	void deletee()
	{
		if(head==NULL)
		{
		cout<<"list is empty\n";
	    }
	    else if(head==last)
	    {
	    	cout<<head->data<<" is deleted\n";
	    	head=NULL;
	    	last=NULL;
		}
		else
	    {
	    	cout<<last->data<<" is deleted\n";
	    	last=last->previous;
	    	last->next=head;
	    	head->previous=last;
		}
	}
	void deleten()
	{
		if(head==NULL)
		{
			cout<<"list is empty\n";
		}
		else
		{
			int a,i;
			node *temp1=new node;
			node *nbl=new node;
			temp1=head;
			nbl=head;
			cout<<"enter position to be deleted\n";
			cin>>a;
			if(a==1&&head->next==NULL)
			{
				cout<<head->data<<"is deleted\n";
				head=NULL;
			}
				else if(a==1)
				{
					cout<<temp1->data<<"is deleted\n";
					head=head->next;
				}
				else
				{
					i=1;
					while(i<a)
					{
						nbl=temp1;
						temp1=temp1->next;
						i++;
					}
					cout<<temp1->data<<"is deleted\n"<<endl;
					nbl->next=temp1->next;
					temp1->next->previous=nbl;
				}
			}
	    }
	void search()
	{
		if(head==NULL)
		{
			cout<<"list is empty\n";
		}
		else
		{
			int x,i=0;
		    node *temp1=new node;
			temp1=head;
			cout<<"enter element to be searched\n";
			cin>>x;
			while(temp1!=last)
		    {
		    	if(temp1->data==x)
		    	{
		    		i=1;
		    		break;
				}
				else
			    temp1=temp1->next;
			}
			if(temp1->data==x)
			{
			i=1;
		    }
			if(i==1)
			{
				cout<<"element is present\n";
			}
			else
			{
				cout<<"no element found\n";
			}
		}
	}
	void display()
	{
		if(head==NULL)
		{
			cout<<"list is empty\n";
		}
		else
		{
			node *temp1=new node;
			temp1=head;
			while(temp1!=last)
			{
				cout<<temp1->data<<"->";
				temp1=temp1->next;
			}
			cout<<last->data<<"\n";
		    cout<<"list in reverse order:\n";
		    node *temp=new node;
		    temp=last;
		while(temp!=head)
		{
			cout<<temp->data<<"->";
			temp=temp->previous;
		}
		cout<<temp->data<<"\n";
	    }
    }
};
main()
{
	dcll s1;
	int a;
	while(a!=9)
	{
		cout<<"1.insert at begin\n2.insert at end\n3.insert at any where\n4.delete at begin\n5.delete at end\n6.delete at anywhere\n7.search\n8.display\n9.exit\n";
		cout<<"enter your choice\n";
		cin>>a;
		switch(a)
		{
			case 1:
			s1.insertf();
			break;
			case 2:
			s1.inserte();
			break;
			case 3:
			s1.insertn();
			break;
			case 4:
			s1.deletef();
			break;
			case 5:
			s1.deletee();
			break;
			case 6:
			s1.deleten();
			break;
			case 7:
			s1.search();
			break;
			case 8:
			s1.display();
			break;	
		}
	}
}
