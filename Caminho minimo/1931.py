class MST:

    def __init__(self, vertices):
        self.Vertices = vertices
        self.grafo = []
        for i in range(vertices):
            self.grafo.append([])
            for j in range(vertices):
                self.grafo[i].append(0)

    def addEdge(self, v1, v2, peso):
        self.grafo[v1][v2] = peso
        self.grafo[v2][v1] = peso

    def printSolution(self, dist2):
        if dist2[self.Vertices-1] == float('inf'):
            print("-1")
        else:
            print(dist2[self.Vertices-1])

    def minDistance(self, dist, sptSet):
        min_index = 0
        min = float('inf')

        for v in range(self.Vertices):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.Vertices
        dist2 = [float('inf')] * self.Vertices
        dist[src] = 0
        dist2[src] = 0
        counter = 0
        sptSet = [False] * self.Vertices

        for cout in range(self.Vertices):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.Vertices):
                if self.grafo[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.grafo[u][v]:
                    dist[v] = dist[u] + self.grafo[u][v]
                    counter += 1
                if counter % 2 == 1:

                    dist2[v] = dist[v]

        self.printSolution(dist2)


vertice, linha = input().split()
vertice, linha = map(int, [vertice, linha])
g = MST(vertice)
for i in range(linha):
    v1, v2, peso = input().split()
    v1, v2, peso = map(int, [v1, v2, peso])
    g.addEdge(v1-1, v2-1, peso)
g.dijkstra(0)