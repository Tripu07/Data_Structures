class node:
    def __init__(self,data):
        self.pref=None
        self.nref=None
        self.data=data
class doubly_linked_list:
    def __init__(self):
        self.head=None
    def forward_traversal(self):
        if self.head==None:
            print("Doubly linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.nref
    def backward_traversal(self):
        if (self.head==None):
            print("Doubly linked list is empty")
        else:
            temp=self.head
            while temp.nref is not None:
                temp=temp.nref
        while temp is not None:
            print(temp.data)
            temp=temp.pref
        
    def insert_first_node(self,data):
        newnode=node(data)
        temp=self.head
        newnode.nref=temp
        temp.pref=newnode
        self.head=newnode
    def insert_last_node(self,data):
        newnode=node(data)
        temp=self.head
        while temp.nref is not None:
                temp=temp.nref
        temp.nref=newnode
        newnode.pref=temp
    def insert_any_position(self,data,x):
        newnode=node(data)
        temp=self.head
        i=1
        while(i<x):
            temp=temp.nref
            i=i+1
        newnode.nref=temp.nref
        newnode.pref=temp
        temp.nref.pref=newnode
        newnode.nref=temp.nref
        temp.nref=newnode
    def delete_first_node(self):
        temp=self.head
        temp=temp.nref
        temp.pref=None
        self.head=temp
    def delete_last_node(self):
        temp=self.head
        while temp.nref.nref is not None:
            temp=temp.nref
        temp.nref=None
    def delete_any_position(self,x):
        temp=self.head
        i=1
        while(i<x):
            temp=temp.nref
            k=temp.nref.nref
            i=i+1
        temp.nref=k
        k.pref=temp
            
        
            
        
        
    
    
            
        
        
        
        

d1=doubly_linked_list()
n1=node(1)
n2=node(2)
n3=node(3)
d1.head=n1
n1.nref=n2
n2.pref=n1
n2.nref=n3
n3.pref=n2

#d1.insert_first_node(5)
d1.insert_last_node(6)
d1.insert_any_position(2.5,3)
#d1.delete_first_node()
#d1.delete_last_node()
d1.delete_any_position(2)
d1.forward_traversal()
#d1.backward_traversal()

            
