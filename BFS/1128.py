loop = True
from collections import defaultdict
class IreVir:
  def __init__(self, N):
    self.N = N
    self.grafo = defaultdict(list)
    self.res = 0
    self.count = 0
    for i in range(N):
      self.grafo[i] = []
    return

  def addEdge(self,u,v,*args):
    if(args[0] == 2):
      self.grafo[v].append(u)
    self.grafo[u].append(v)
    return
  def resFunc(self, u, comp1, comp2, binStack, stack):
      if self.res >= 2:
          return False
      comp2[u] = self.count
      comp1[u] = self.count
      self.count += 1
      binStack[u] = True
      stack.append(u)

      for v in self.grafo[u]:
          if comp2[v] == -1:
              self.resFunc(v, comp1, comp2, binStack, stack)
              comp1[u] = min(comp1[u], comp1[v])
          elif binStack[v]: #se verdadeiro stacka
              comp1[u] = min(comp1[u], comp2[v])

      w = -1
      if (comp1[u] == comp2[u]):
          while (w != u): #tira da pilha o vertice do topo
              w = stack.pop()
              binStack[w] = False
          self.res += 1

  def irvir(self):
      binStack = [False] * (self.N)
      stack = []
      comp2 = [-1] * (self.N)
      comp1 = [-1] * (self.N)
      for i in range(self.N):
          if self.res >= 2:
              return None
          if comp2[i] == -1:
              self.resFunc(i, comp1, comp2, binStack, stack)
  def printMatrix(self):
      for i in range(self.N):
          print(self.grafo[i])

  
while(loop):
  x, y = input().split()
  x, y = map(int, [x,y])
  if((x and y) == 0):
    loop = False
    break
  else:
    i1 = IreVir(x)
    for i in range(y):
      v,w,p = input().split()
      v, w, p = map(int, [v,w,p])
      i1.addEdge(v-1,w-1,p)
    
    i1.irvir()

    if (i1.res == 1):
      print("1")
    else:
      print("0")