class bst:
    def __init__(self):
        self.root=[0]
    def add(self):
        a=int(input('Enter data:'))
        if len(self.root)==1:
            self.root.append(a)
        else:
            j=1
            while self.root[j]!=0:
                if a>self.root[j]:
                    j=j*2+1
                    if j>=len(self.root):
                        i=len(self.root)-1
                        while(i<j):
                            self.root.append(0)
                            i=len(self.root)-1
                elif a<self.root[j]:
                    j=j*2
                    if j>=len(self.root):
                        i=len(self.root)
                        while(i<=j+1):
                            self.root.append(0)
                            i=len(self.root)
                else:
                    print(a,end=' is already existed\n')
                    break
            self.root[j]=a
            print(a,end=' is added successfully!\n')
    def preorder(self,j):
        if j<len(self.root):
            if self.root[j]!=0:
                print(self.root[j],end=' ')
        if j<len(self.root):
            self.preorder(j*2)
        
        if j<len(self.root):
            self.preorder(j*2+1)
    def search(self,a):
        j=1
        while(self.root[j]!=a and self.root[j]!=0 and j<len(self.root)):
            if a>self.root[j]:
                j=j*2+1
            elif a<self.root[j]:
                j=j*2
            if j>=len(self.root):
                break
        if j>=len(self.root):
            return 0
        elif j<len(self.root):
            return 1
b1=bst()
while 1:
    i=int(input('\n1.add an element\n2.preorder\n3.search\nEnter your choice:'))
    if i==1:
        b1.add()
    elif i==2:
        b1.preorder(1)
    elif i==3:
        a=int(input('Enter number to search:'))
        s=b1.search(a)
        if s==1:
            print(a,end=' is found\n')
        elif s==0:
            print(a,end= ' is not found\n')
    else:
        break
