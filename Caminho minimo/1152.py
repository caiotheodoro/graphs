flag = 1
class MST:
 
    def __init__(self, vertices):
        self.Vertices = vertices
        self.graph = []
        self.aux = []
        self.max = 0
        self.min = 0

    def addEdge(self, v1, v2, peso):
        self.graph.append([v1, v2, peso])
        self.max = self.max + peso

    def find(self, parente, i):  # retorna o pai de um determinado vertice
        if parente[i] == i:
            return i
        return self.find(parente, parente[i])

    def uni(self, parente, rank, x, y):
        x = self.find(parente, x)
        y = self.find(parente, y)
        if rank[x] < rank[y]:
            parente[x] = y
        elif rank[x] > rank[y]:
            parente[y] = x
        else:
            parente[y] = x
            rank[x] += 1
 
    def kruskal(self):
        i = 0
        e = 0
        parente = [i for i in range(self.Vertices)]
        rank = [0] * self.Vertices
        # ordena por peso
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.Vertices - 1:  # enquanto ainda nao chegar ao fim da lista
            v1, v2, peso = self.graph[i]
            i += 1
            x = self.find(parente, v1)
            y = self.find(parente, v2)
            if x != y:  # para evitar ciclos
                e = e + 1
                self.aux.append([v1, v2, peso])
                self.uni(parente, rank, x, y)
        for v1, v2, peso in self.aux:
            self.min += peso
 
while flag==1:
    vertice, linha = input().split()
    vertice, linha = map(int, [vertice, linha])
    if vertice == 0 and linha == 0:
        flag = 0
        break
    else:
        g = MST(vertice)
        for i in range(linha):
            v1, v2, peso = input().split()
            v1, v2, peso = map(int, [v1, v2, peso])
            g.addEdge(v1, v2, peso)

        g.kruskal()
        print(g.max - g.min)