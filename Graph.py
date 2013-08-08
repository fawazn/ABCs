'''Python implementation of a Graph data structure, features Breadth first search,
Depth First search, and terrible spelling.'''

import queue

class Graph:
    def __init__(self,Vr,Ed,VertList):
        self.N_Vertices = Vr
        self.N_Edges = Ed
        self.Vertlist  = VertList
        self.AdjList = []
        for x in filter(lambda y: y%2 == 0,range(len(self.Vertlist)-1)):
            self.AdjList.extend([[],[]])
            self.AddEdge(VertList[x],VertList[x+1])
    def fget(self):
        return self.N_Vertices
    def E(self):
        return self.N_Edges
    def adjacent(self,vertex):
        return self.AdjList[vertex]
    def AddEdge(self,Vert1,Vert2):
        self.AdjList[Vert1].append(Vert2)
        self.AdjList[Vert2].append(Vert1)
        self.N_Edges += 1

#Simple DFS: find all connected vertices
def SearchDepthFirst(Graph,Vertex):
    count = 0
    EdgeTo = [None]*Graph.N_Vertices
    marked = [False]*Graph.N_Vertices
    def DepthFirstSearch (incomingGraph, vertex):
        marked[vertex] = True
        nonlocal count
        nonlocal EdgeTo
        count += 1
        for adjvertex in incomingGraph.adjacent(vertex):
            if not marked[adjvertex]:
                EdgeTo[adjvertex] = vertex
                DepthFirstSearch(incomingGraph, adjvertex)
    def BreathFirstSearch (incomingGraph, vertex):
        marked[vertex] = True
        vq = queue()
        vq.enqueue(vertex)
        while not vq.Empty():
            v = vq.dequeue()
            for adjvertex in incomingGraph.adjavent(vertex):
                if not marked[adjvertex]:
                    vq.enqueue(adjvertex)
                    marked[adjvertex] = True
                    EdgeTo[adjvertex] = v

    def PathToVertex(start, end):
        if not marked[end]: return None
        i = end
        path = []
        while i != start:
            if i == None: break
            path.append(i)
            i = EdgeTo[i]
        path.append(start)
        return path

    DepthFirstSearch(Graph,Vertex)
    for v in range(GraphToSearch.N_Vertices):
        if marked[v]:
            print (v," ")
    return PathToVertex


GraphToSearch = Graph(7,6,[0,1,1,2,0,3,3,4,1,2,5,6,5,7])
NodeIsland = SearchDepthFirst(GraphToSearch,0)
print (NodeIsland(2,4))






