class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head==None:
            print("empty list")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)#it prints the data of node which hass adress location equal to temp
                temp=temp.ref  #now new value of temp is ref which is stored in next node
    def insert_node_first(self,data):
        newnode=node(data)
        newnode.ref=self.head  #old value of self.head will be equal to new node.ref
        self.head=newnode   #  new adress stored in head is equal to the location /adress of newnode
    def delete_node_first(self):
        temp=self.head
        self.head=temp.ref
    def insert_node_last(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.ref is not None:   #untill 
                temp=temp.ref
            temp.ref=newnode
    def delete_last_node(self):
        temp=self.head
        if(temp.ref==None):
            self.head=None
        else:
            while temp.ref.ref is not None:   #we will have to check the reference of next to node because if we delete last node then reference of second last node becomes None/null
                temp=temp.ref
            temp.ref=None
    def insert_after_nodes(self,data,x):
        newnode=node(data)
        temp=self.head
        i=1
        while(i<x):   #x is the  position where you want to insert a node  ,considering the fact that index of node starts from zero 
            temp=temp.ref
            i=i+1
        newnode.ref=temp.ref
        temp.ref=newnode
        
            
        
                
        
            
        
                
      
                
                
        
        
        
        
        

l1=linkedlist()  #created an object of linked list
n1=node(1)
l1.head=n1    #adress stored in head is equal to location/adress of n1
n2=node(2)
n1.ref=n2  #adress inside n1 is equal to location of n2, hence we equate
n3=node(3)
n2.ref=n3   #adress inside n2 is equal to location of n3, hence we equate
#l1.insert_node(4)
l1.insert_node_last(6)
l1.delete_last_node()
l1.insert_after_nodes(2.5,0)
l1.traversal()


