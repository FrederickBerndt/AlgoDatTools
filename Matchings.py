def Matchings(graph):
    matchedNodes = set()
    resultList = []
    for edge in graph:
        if not (edge[0] in matchedNodes or edge[1] in matchedNodes):
            resultList.append(edge)
            matchedNodes.add(edge[0])
            matchedNodes.add(edge[1])
    return resultList

print(Matchings([(0,1),(0,2),(1,2),(2,3)]))