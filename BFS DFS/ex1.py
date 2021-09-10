loop = True
from collections import defaultdict
class Graph:
  def __init__(self, vertices):
    self.Vertice = vertices
    self.grafo = defaultdict(list)
    self.res = []
    for i in range(vertices):
      self.grafo[i] = []
    return

  def addEdge(self,u,v):
    self.grafo[u].append(v)
    return

  def BFS(self, s):
    
        visited = [False] * (self.Vertice + 1)
 
        stack = []
 
        stack.append(s)
        visited[s] = True
 
        while stack:
 
            s = stack[0]
            del stack[0]
            self.res.append(s)

            for i in self.grafo[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True

        for i in self.res:
            print(i, end = ' ')

  def printMatrix(self):
      for i in range(self.Vertice):
          print(self.grafo[i])

  