import queue
graph={}  #adjacency list
nodes=[]
node_count=0
a1=[]
a2=[]
stack=queue.LifoQueue()
def insert_node(data):  #Insertion of node  #CREATING A adjacency list
    global node_count
    global graph
    node_count=node_count+1
    nodes.append(data)
    for i in range(node_count):
        a1.append([])
        graph[data]=a1[i]
def print_graph():   
    print(graph)

def insert_edge(a,b):#INSERTION OF EDGE BETWEEN TWO GIVEN NODES  ,wth weighted edges
    if a and b in nodes:
        temp1=nodes.index(a)
        temp2=nodes.index(b)
        a1[temp1].append(b)
        a1[temp2].append(a)
def delete_node(data):
    if data in nodes:
        global node_count
        node_count=node_count-1
        nodes.remove(data)
        graph.pop(data)
        for i in a1:
            for j in i:
                if j==data:
                    i.remove(j)
def delete_edge(a,b):
    if a and b in nodes:
        temp1=nodes.index(a)
        temp2=nodes.index(b)
        a1[temp1].remove(b)
        a1[temp2].remove(a)
def traversal(a):    #we will have to mention the node where we want to start 
    global node_count
    if a not in nodes:
        print("Node not present")
        return
    l1=graph[a]
    if a not in a2:
        a2.append(a)
    
    if len(a2)==node_count:  #base condition 
        return
    else:
        for i in l1:
            if i not in a2:
                stack.put(i)
    a=stack.get()#backtracking
    traversal(a)
    return a2
    
    
    
    
insert_node("A")
insert_node("B")
insert_node("C")
insert_node("D")
insert_node("E")
insert_edge("A","B")
insert_edge("C","D")
insert_edge("A","C")
insert_edge("B","D")
insert_edge("A","D")
insert_edge("B","E")
insert_edge("B","D")
insert_edge("D","E")
#delete_node("C")
#delete_edge("A","B")
print(nodes)
print_graph()
print(traversal("A"))
print(node_count)
    
