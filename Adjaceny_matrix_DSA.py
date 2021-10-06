global nodes
global graph
global node_count
nodes=[] #key(data stored)of all  nodes is stored in this list
graph=[]   #Adjacency matrix  #No of nodes
node_count=0 #no of nodes
def insert_node(n):
    global node_count
    global nodes
    global graph
    if n in nodes:
        print("Data already present")
    else:
        node_count=node_count+1
        nodes.append(n)
        for i in graph:
            i.append(0)
        a1=[]
        for i in range(node_count):
            a1.append(0)
        graph.append(a1)
def insert_edge(a,b):
    if a and b in nodes:
        temp1=nodes.index(a)
        temp2=nodes.index(b)
        graph[temp1][temp2]=1
        graph[temp2][temp1]=1
    else:
        print("No such nodes present")
def print_graph():
    for i in graph:
        for j in i:
            print(j,end=" ")
        print()
insert_node("a")
insert_node("b")
insert_node("c")
insert_node("d")
insert_edge("a","b")
insert_edge("c","d")
insert_edge("a","c")
insert_edge("d","b")
print(nodes)
print_graph()


        
        
