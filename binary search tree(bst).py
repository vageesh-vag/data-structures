class node:
    def __init__(self):
        self.data=0
        self.next=None
        self.prev=None
class bst:
    def __init__(self):
        self.root=None
    def add(self):
        self.a=int(input('Enter data:'))
        self.new=node()
        self.new.data=self.a
        if self.root is None:
            self.root=self.new
            print(self.a,end=' is added sucessfully!\n')
        else:
            self.iterate(self.root)

    def iterate(self,temp):
        if self.a>temp.data:
            if temp.next is None:
                temp.next=self.new
                print(self.a,end=' is added sucessfully!\n')
            else:
                self.iterate(temp.next)
        elif self.a<temp.data:
            if temp.prev is None:
                temp.prev=self.new
                print(self.a,end=' is added sucessfully!\n')
            else:
                self.iterate(temp.prev)
        else:
            print(self.a,end=' is already existed!')
    def preorder(self,temp=None):
        if temp is None:
            print(self.root.data,end=' ')
            if self.root.prev is not None:
                self.preorder(temp=self.root.prev)
            if self.root.next is not None:   
                self.preorder(temp=self.root.next)
        else:
            print(temp.data,end=' ')
            if temp.prev is not None:
                self.preorder(temp=temp.prev)
            if temp.next is not None:
                self.preorder(temp=temp.next)
    def search2(self,b):
        s=0
        temp=self.root
        while temp is not None:
            if temp.data==b:
                s=1
                break
            else:
                if b>temp.data:
                    temp=temp.next
                elif b<temp.data:
                    temp=temp.prev
        return s
    def delete(self,a):
        temp=self.root
        temp1=self.root
        while temp is not None:
            if temp.data==a:
                break
            else:
                temp1=temp
                if a>temp.data:
                    temp=temp.next
                elif a<temp.data:
                    temp=temp.prev
        if temp.next is None and temp.prev is None:
            if temp1.next is not None:
                if temp1.next.data==temp.data:
                    temp1.next=None
            if temp1.prev is not None:
                if temp1.prev.data==temp.data:
                    temp1.prev=None
            print(temp.data,end=' is deleted sucessfully!\n')
        elif temp.next is None or temp.prev is None:
            if temp1.next is not None:
                if temp1.next.data==temp.data:
                    if temp.next is None:
                        temp1.next=temp.prev
                    elif temp.prev is None:
                        temp1.next=temp.next
            if temp1.prev is not None:
                if temp1.prev.data==temp.data:
                    if temp.next is None:
                        temp1.prev=temp.prev
                    elif temp.prev is None:
                        temp1.prev=temp.next
            print(temp.data,end=' is deleted sucessfully!\n')
        elif temp.next is not None and temp.prev is not None:
            if temp.next.prev is None:
                if temp1.next is not None:
                    if temp1.next.data==temp.data:
                        temp1.next=temp.next
                        temp.next.prev=temp.prev
                if temp1.prev is not None:
                    if temp1.prev.data==temp.data:
                        temp1.prev=temp.next
                        temp.next.prev=temp.prev
                print(temp.data,end=' is deleted sucessfully!\n')
            else:
                temp2=temp.next
                temp3=temp.next
                while temp2.prev is not None:
                    temp3=temp2
                    temp2=temp2.prev
                if temp1.next is not None:
                    if temp1.next.data==temp.data:
                        temp1.next=temp2
                        temp3.prev=temp2.next
                        temp2.prev=temp.prev
                        temp2.next=temp.next
                if temp1.prev is not None:
                    if temp1.prev.data==temp.data:
                        temp1.prev=temp2
                        temp3.prev=temp2.next
                        temp2.prev=temp.prev
                        temp2.next=temp.next
                print(temp.data,end=' is deleted sucessfully!\n')
b1=bst()
while 1:
    a=int(input('\n1.add element\n2.preorder traversal\n3.search\n4.delete\n5.exit\nEnter your choice:'))
    if a==1:
        b1.add()
    elif a==2:
        b1.preorder()
    elif a==3:
        i=int(input('Enter num to search:'))
        s=b1.search2(i)
        if s==1:
            print(i,end=' is found\n')
        else:
            print(i,end=' is not found\n')
    elif a==4:
        i=int(input('Enter num to delete:'))
        s=b1.search2(i)
        if s==1:
            b1.delete(i)
        else:
            print(i,end=' is not found\n')
    else:
        break
