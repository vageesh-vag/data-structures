class node:
    def __init__(self):
        self.data=0
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.root=None
    def insertf(self):
        a=int(input('Enter data:'))
        new_node=node()
        new_node.data=a
        if self.root==None:
            self.root=new_node
        else:
            new_node.next=self.root
            self.root.prev=new_node
            self.root=new_node
    def inserte(self):
        a=int(input('Enter data:'))
        new_node=node()
        new_node.data=a
        if self.root==None:
            self.root=new_node
        else:
            temp=self.root
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def insertany(self):
        a=int(input('Enter data:'))
        new_node=node()
        new_node.data=a
        if self.root==None:
            self.root=new_node
        else:
            pos=int(input('Enter position:'))
            if pos==1:
                new_node.next=self.root
                slef.root.prev=new_node
                self.root=new_node
            else:
                temp=self.root
                temp1=self.root
                i=1
                while(i<pos):
                    temp1=temp
                    temp=temp.next
                    i=i+1
                temp1.next=new_node
                new_node.prev=temp1
                new_node.next=temp
                temp.prev=new_node
                
    def deletef(self):
        if self.root is None:
            print('list is empty')
        else:
            print(self.root.data,end=' is deleted sucessfully!\n')
            self.root=self.root.next
            self.root.prev=None
    def deletee(self):
        if self.root is None:
            print('list is empty')
        elif self.root.next is None:
            print(self.root.data,end=' is deleted sucessfully!\n')
            self.root=None
        else:
            temp1=self.root
            temp=self.root
            while temp.next is not None:
                temp1=temp
                temp=temp.next
            temp.prev=None
            temp1.next=None
            print(temp.data,end=' is deleted successfully!\n')
    def delpos(self):
        pos=int(input('Enter position'))
        if pos==1:
            self.root=self.root.next
            sel.root.prev=None
        else:            
            i=1
            temp=self.root
            temp1=self.root
            while i<pos:
                temp1=temp
                temp=temp.next
                i=i+1
            print(temp.data,end=' is deleted successfully!\n')
            temp.next.prev=temp1
            temp1.next=temp.next
        
    def delele(self,a):
        if self.root.data==a:
            self.root=self.root.next
        else:
            temp=self.root
            temp1=self.root
            while temp.data!=a:
                temp1=temp
                temp=temp.next
            temp.next.prev=temp1
            temp1.next=temp.next
    def search(self,a):
        s=0
        if self.root is None:
            print('list is empty')
        elif a==self.root.data:
            s=1
        else:
            temp=self.root
            while temp.next is not None:
                if a==temp.data:
                    s=1
                    break
                else:
                    temp=temp.next
            if a==temp.data:
                s=1
        return s
            
    def display(self):
        temp=self.root
        while temp.next is not None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)
    def displayr(self):
        temp=self.root
        while temp.next is not None:
            temp=temp.next
        while temp.prev is not None:
            print(temp.data,end='->')
            temp=temp.prev
        print(temp.data)
    def sortl(self):
        temp=self.root
        temp1=self.root
        i=0
        a=[]
        while temp is not None:
            a.append(temp.data)
            temp=temp.next
        b=int(input('1.ascending order\n2.descending order\nEnter your choice:'))
        if b==1:
            a.sort()
        elif b==2:
            a.sort(reverse=True)
        while temp1 is not None:
            temp1.data=a[i]
            i=i+1
            temp1=temp1.next
        print('Sorted Sucessfully!')
        
            
s1=sll()
while 1:
    i=int(input('menu\n1.insert at begin\n2.insert at end\n3.insert anywhere\n4.delete at begin\n5.delete at end\n6.delete at anywhere\n7.display\n8.search\n9.sort\n10.exit\nEnter your choice:'))
    if i==1:
        s1.insertf()
        pass
    elif i==2:
        s1.inserte()
        pass
    elif i==3:
        s1.insertany()
        pass
    elif i==4:
        s1.deletef()
        pass
    elif i==5:
        s1.deletee()
        pass
    elif i==6:
        b=int(input('1.delete by index\n2.delete by element\nselect your choice:'))
        if b==1:
            s1.delpos()
        elif b==2:
            c=int(input('Enter element to delete:'))
            s=s1.search(c)
            if s==1:
                s1.delele(c)
                print(c,end=' is deleted successfully!\n')
            else:
                print(c,end=' is not found!\n')
        pass
    elif i==7:
        d=int(input('1.display from front\n2.display in reverse\nEnter your choice:'))
        if d==1:
            s1.display()
        elif d==2:
            s1.displayr()
        pass
    elif i==8:
        a=int(input('Enter a num to search:'))
        s=s1.search(a)
        if s==1:
            print(a,end=' is found\n')
        else:
            print(a,end=' is not found\n')
        pass
    elif i==9:
        s1.sortl()
        pass
    else:
        break
