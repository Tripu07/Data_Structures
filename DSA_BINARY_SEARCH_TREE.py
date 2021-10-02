class bst:   #definition of a node =>definition of BST  because we don't have othe variables in BST
    def __init__(self,key):
        self.key=key
        self.rchild=None
        self.lchild=None
    def insert(self,data):
        if self.key is None:    #"self" here is an object ,any object that uses this method will be replaced by "self" in execution phase
            self.key=data
            return
        if self.key >data:
            if self.lchild is not None:
                self.lchild.insert(data)  #recursive approach 
            else:
                newnode=bst(data)
                self.lchild=newnode
        else:
            if self.rchild is not None:
                self.rchild.insert(data)  #If there is branching at any node then we should know that now we have to compare with respective parent node as root node
            else:
                newnode=bst(data)
                self.rchild=newnode
                #look the point you have to look over root /parent nodes if there is branching at root /parent node you have to follow same set of instructions and this is recursive property
    def search(self,x):
        if self.key is None:
            print("Empty tree:Data not found ")
            return    #return is used here to exit the function otherwise it takes on methods/next steps again 
        if self.key==x:
            print("Data found")
            return 
        if self.key < x:
            if self.rchild is not None:
                self.rchild.search(x)
            else:
                print("Data not found")
        else:
            if self.lchild is not None:
                self.lchild.search(x)
            else:
                print("Data not found")
    def pre_order_traversal(self):
        if self.key is None:
            print("Empty Tree")
            return
        if self.key is not None:
            print(self.key)
        if self.lchild is not None:
            self.lchild.pre_order_traversal()  #recursion taking place ,after every branching our root node changes ,and due to this all code is executed again when finally this execution phase
            #is over the code jumps to self.rchild condition 
        if self.rchild is not None:
            self.rchild.pre_order_traversal()
    def in_order_traversal(self):
        if self.key is None:
            print("Empty tree")
            return
        if self.lchild is not None:
            self.lchild.in_order_traversal()
        
        if self.rchild is not None:
            print(self.key)
            self.rchild.in_order_traversal()
        else:
            print(self.key)
        
    def post_order_traversal(self):
        if self.key is None:
            print("Empty tree")
            return
        if self.lchild is not None:
            self.lchild.post_order_traversal()
        if self.rchild is not None:
            self.rchild.post_order_traversal()
        print(self.key)
    def level_traversal(self):
        print(self.key)
        if self.lchild and self.rchild:
            print(self.lchild.key)
            print(self.rchild.key)
    def delete_node(self,x):
        if self.key is None:
            print("Empty tree")
            return
                      
        if self.key >x:
            if self.lchild:
                self.lchild=self.lchild.delete_node(x)  #this method will return the adress of the node which would be attached later after deletion
            else:
                print("No node found to be deleted")
        elif self.key<x:
            if self.rchild:
                self.rchild=self.rchild.delete_node(x)
            else:
                print("No node found to be deleted")
        else:
            if self.lchild is  None:
                temp=self.rchild
                self=None  #Direct use of object(here "self") means adress of that object 
                return temp
            if self.rchild is  None:
                temp=self.lchild
                self=None
                return temp
            node=self.lchild
            while(node.rchild is not None):
                node=node.rchild
            self.key=node.key
            self.lchild=self.lchild.delete_node(node.key)
            return self
    def min_max(self):
        if self.lchild:
            temp=self.lchild
            while temp.lchild is not None:
                temp=temp.lchild
            print(f"Minimum value :{temp.key}")
        else:
            print(f"Minimum value :{self.key}")
        if self.rchild:
            temp=self.rchild
            while temp.rchild is not None:
                temp=temp.rchild
            print(f"Maximum value :{temp.key}")
        else:
            print(f"Maximum value :{self.key}")
                

                
                    
            
            
            
            
        
            
       
            
        
               

    
            
        
           
                    

root=bst(10)
l1=[12,2,8,16,17]
for i in l1:
    root.insert(i)
#root.search(30)
#root.pre_order_traversal()
#root.in_order_traversal()
#root.post_order_traversal()
#root.level_traversal()
#root.delete_node(16)
#root.in_order_traversal()
root.min_max()
            
