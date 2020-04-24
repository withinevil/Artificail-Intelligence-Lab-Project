from pip._vendor.distlib.compat import raw_input

dict_graph = {}


# Read the data.txt file
with open('data.txt', 'r') as f:
    for l in f:
        city_a, city_b, p_cost = l.split()
        if city_a not in dict_graph:
            dict_graph[city_a] = {}
        dict_graph[city_a][city_b] = int(p_cost)
        if city_b not in dict_graph:
            dict_graph[city_b] = {}
        dict_graph[city_b][city_a] = int(p_cost)


# Breadth First Search Method
def BreadthFirstSearch(graph, src, dst):
    q = [(src, [src], 0)]
    visited = {src}
    while q:
        (node, path, cost) = q.pop(0)
        for temp in graph[node].keys():
            if temp == dst:
                return path + [temp], cost + graph[node][temp]
            else:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))


# Depth First Search Method
def DepthFirstSearch(graph, src, dst):
    stack = [(src, [src], 0)]
    visited = {src}
    while stack:
        (node, path, cost) = stack.pop()
        for temp in graph[node].keys():
            if temp == dst:
                return path + [temp], cost + graph[node][temp]
            else:
                if temp not in visited:
                    visited.add(temp)
                    stack.append((temp, path + [temp], cost + graph[node][temp]))




n = 1
print (dict_graph)
print ("------------------------------------------------")
while n == 1:
    name = input("Enter the Type of Search you Want \n1.BFS 2.DFS  \n ")
    if name == "BFS":
        src = raw_input("Enter the source: ")
        dst = raw_input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = raw_input("Enter the correct source (case_sensitive):\n")
            dst = raw_input("Enter the correct destination(case_sensitive):\n ")
        print("for BFS")
        print(BreadthFirstSearch(dict_graph, src, dst))

    elif name == "DFS":
        src = raw_input("Enter the source: ")
        dst = raw_input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = raw_input("Enter the correct source (case_sensitive):\n")
            dst = raw_input("Enter the correct destination(case_sensitive):\n ")
        print("for DFS")
        print(DepthFirstSearch(dict_graph, src, dst))


