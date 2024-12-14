from networkx import DiGraph
def isAcyclicNX(graph):
    S=[]
    for e in graph.nodes:
        if graph.out_degree(e) == 0:                # unknown Runtime
            S.append(e)
    while S:
        v = S.pop()
        for e in graph.in_edges(v):                 # unknown Runtime
            if graph.out_degree(e[0]) == 1:         # unknown Runtime
                S.append(e[0])
        graph.remove_node(v)                        # unknown Runtime
    return graph.number_of_nodes() == 0             # unknown Runtime
     

def isAcyclicExplicit(graph):                       # in O(n+m)
    nodeList = []
    S = []
    n = len(G.edges)
    for i in range(n): nodeList.append([0,[]])      # in O(n)
    for edge in graph.edges:                        # in O(m)
        nodeList[edge[0]][0] += 1
        nodeList[edge[1]][1].append(edge[0])
    for i in range(n):                              # in O(n)
        if nodeList[i][0] == 0: S.append(i)
    while len(S) != 0:                              # in O(m)
        v = S.pop()
        n -= 1
        for i in nodeList[v][1]:                    # in O(indeg(v))
            nodeList[i][0] -= 1
            if nodeList[i][0] == 0:
                S.append(i)
    return n==0

G = DiGraph()
G.add_edges_from([(0,1),(0,2),(1,2)])
print(isAcyclicNX(G))