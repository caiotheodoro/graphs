loop = True
contador = 1

class Dengue:
    def __init__(self, N):
        self.N = N
        self.grafo = [[] for i in range(N)]
        self.count = 0
        self.dist = [0]*self.N
        self.temp = 0
        self.visitados = [False]*N
        return

    def addEdge(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
        return

    def BFS(self,u,cont):
        cont+=1
        self.visitados[u] = True

        for i in self.grafo[u]:
            if not self.visitados[i]:
                self.temp += cont
                self.BFS(i,cont+1)
        return self.temp       

    def BFS_step(self):
        for i in range(self.N):
            self.temp = 0 
            self.visitados = [False]*self.N
            self.dist[i] =  self.BFS(i,0)


while(loop):
    x = int(input())
    if x == 1:
    
        print("Teste",contador,":")
        print("1")
        loop = False
        break
    else:
        d1 = Dengue(x)
        for i in range(x-1):
            u, v = input().split()
            u, v = map(int, [u, v])
            d1.addEdge(u-1, v-1)

        d1.BFS_step()
        print("Teste",contador,":")
        print(d1.dist.index(min(d1.dist))+1)
        contador += 1
            
