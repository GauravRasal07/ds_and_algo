#DFS and BFS graph traversals using adjacency list for graph representation

graph = {
    "A" : ['B', 'C'],
    "B" : ['A', 'D', 'E'],
    "C" : ['A', 'F', 'G'],
    "D" : ['B'],
    "E" : ['B'],
    "F" : ['C'],
    "G" : ['C'],
}


bfs_visited = []
q = []

def bfs(start):
    q.append(start)
    # bfs_visited.append(start)
    path = []
    
    while q:
        node = q.pop(0)
        # print("Node: ", node)
        
        if node not in bfs_visited:
            bfs_visited.append(node)
            
        for adj_node in graph[node]:
            if adj_node not in bfs_visited:
                q.append(adj_node)
                bfs_visited.append(adj_node)
    
    print("BFS traversal is: ", bfs_visited)
    
   
dfs_visited = []

def dfs(start):
    if start not in dfs_visited:
        dfs_visited.append(start)
        
        for adj_node in graph[start]:
            dfs(adj_node)
            
    
    
bfs("A")
dfs("A")
print("DFS Traversal is: ", dfs_visited)

#DFS Non-Recursive
def dfs(graph,startNode):
    visited = []
    stack = []
    stack.append(startNode)

    while stack:
        node =stack.pop()
        
        
        if(node not in visited):
            print(node,end=" ")
            visited.append(node)


        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
# dfs(graph, "A")