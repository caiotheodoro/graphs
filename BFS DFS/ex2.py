from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.Vertice = vertices
        self.grafo = defaultdict(list)
        self.res = []
        self.count = 0
        self.visited = [False] * (self.Vertice + 1)
        for i in range(vertices):
            self.grafo[i] = []
        return

    def addEdge(self, u, v):
        self.grafo[u].append(v)
        return

    def DFS_loop(self, s):
        self.res.append(s) 
        self.visited[s] = True
        for i in self.grafo[s]: #Para cada vertice adjacente a s
            if self.visited[i] == False:
                self.DFS_loop(i)
                self.count+=1
                
    def DFS(self,s):
        self.DFS_loop(s)
        for i in self.res:
            print(i, end=' ')

   
        
    def printMatrix(self): 
        for i in range(self.Vertice):
            print(self.grafo[i])
