from collections import defaultdict
class Graph:
  def __init__(self, vertices):
    self.Vertice = vertices
    self.grafo = defaultdict(list)
    self.visited = [False] * (self.Vertice)
    self.visited2 = [False] * (self.Vertice)
    self.res = []
    for i in range(vertices):
      self.grafo[i] = []
    return

  def addEdge(self,u,v):
    self.grafo[u].append(v)
    self.grafo[v].append(u)
    return

    
  def bairro(self,K,L):
      self.visited[K] = True

      for i in self.grafo[K]:
        if i == L:
            self.res.append("Lets que lets")
            return True
        elif self.visited[i] == False:
            
            self.bairro(i,L) 

     
                    

  def bairro_princi(self,K,L):
  
      test = self.bairro2(K,L)
      if (test) != True:
        self.res.append("Deu ruim")


 


N, M, P = input().split()
N, M, P = map(int, [N, M, P])
g = Graph(N)
for i in range(M):
    A, B = input().split()
    A, B = map(int, [A, B])
    g.addEdge(A-1,B-1)
for i in range(P):
    K, L = input().split()
    K, L = map(int, [K, L])
    g.bairro_princi(K-1,L-1)


print(g.res)