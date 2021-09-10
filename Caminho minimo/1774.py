res = [] 
parent = []
rank = []

class MST:
 
    def __init__(self, vertices):
        self.Vertices = vertices  
        self.grafo = []  
       
    def addEdge(self, v1, v2, peso):
        self.grafo.append([v1, v2, peso])
 
 
    def buscaV(self, vet, node):
        if(vet[node] == -1):
            return node
        elif(vet[node] != node):
            vet[node] = self.buscaV(vet, vet[node])
        return vet[node]
 
   
    def uniaoRank(self, parent, rank, pos1, pos2):
               #juncao subonjunto
        if rank[pos1] > rank[pos2]:
            parent[pos2] = pos1
        elif rank[pos1] < rank[pos2]:
            parent[pos1] = pos2
        else:
            parent[pos2] = pos1
            rank[pos1] += 1
 
    def kuskal(self):
        mst = 0 
        i = 0 
        e = 0 
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        for node in range(self.Vertices):
            parent.append(node)
            rank.append(0)
        while e < self.Vertices - 1:
            v1, v2, peso = self.grafo[i]
            i = i + 1
            pos1 = self.buscaV(parent, v1)
            pos2 = self.buscaV(parent, v2)
 
            #confere loop
            if pos1 != pos2:
                e = e + 1
                res.append(peso)
                self.uniaoRank(parent, rank, pos1, pos2)
    
        for  peso in res:
            mst = mst + peso
        print(mst)
 
vertice, linha = input().split()
vertice, linha = map(int, [vertice, linha])
g = MST(vertice)
for i in range(linha):
    v1, v2, peso = input().split()
    v1, v2, peso = map(int, [v1, v2, peso])
    g.addEdge(v1-1, v2-1, peso)

g.kuskal()