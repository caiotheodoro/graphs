class Graph:
    def __init__(self, vertices):
        self.Vertice = vertices
        self.grafo = [[] for i in range(vertices)]
        self.visited = []
        self.res = []
        return

    def addEdge(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
        return

    def bairro(self, K, L):
        self.visited[K] = True
        aux = False

        if K == L:
            self.res.append("Lets que lets")
            aux = True
        else:
            for i in self.grafo[K]:
                if aux == False and self.visited[i] != True:
                    aux = self.bairro(i, L)

        return aux

    def bairro_princi(self, K, L):
        self.visited = [False] * self.Vertice
        test = self.bairro(K, L)

        if not test:
            self.res.append("Deu Ruim")
        return


N,M,P=map(int,input().split())
g=Graph(N)
for i in range(M):
    A,B=map(int,input().split())
    g.addEdge(A-1, B-1)
for i in range(P):
    K,L=input().split()
    K,L=map(int, [K, L])
    g.bairro_princi(K-1, L-1)
    print(g.res[i])