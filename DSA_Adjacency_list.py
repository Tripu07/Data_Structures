graph={}  #adjacency list
nodes=[]
node_count=0
a1=[]
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

def insert_edge(a,b,weight):    #INSERTION OF EDGE BETWEEN TWO GIVEN NODES  ,wth weighted edges
    if a and b in nodes:
        temp1=nodes.index(a)
        temp2=nodes.index(b)
        a1[temp1].append((b,weight))
        a1[temp2].append((a,weight))
def delete_node(data):
    if data in nodes:
        node_count=node_count-1
        nodes.remove(data)
        graph.pop(data)
        for i in a1:
            for j in i:
                for k in j:
                    if k==data:
                        i.remove(j)
def delete_edge(a,b,weight):
    if a and b in nodes:
        temp1=nodes.index(a)
        temp2=nodes.index(b)
        a1[temp1].remove((b,weight))
        a1[temp2].remove((a,weight))
        

        
            
insert_node("A")
insert_node("B")
insert_node("C")
insert_node("D")
insert_edge("A","B",5)
insert_edge("C","D",8)
insert_edge("A","C",9)
insert_edge("B","D",2)
delete_node("C")
delete_edge("A","B",5)
print(nodes)
print_graph()
    
