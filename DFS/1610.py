G = {}
class Documentos:
    def __init__(self, testes):
        self.testes = testes
        return


    def buscaProfundidade(self,G, u):
        vis[u] = 1
        for v in G[u]:
            if v not in vis:
                if self.buscaProfundidade(G, v): return 1
            else: 
                if vis[v] == 1: return 1
        vis[u] = 2
        return 0

    def instancia(self,n,m):
        for i  in range(n):
          G[i] = []
        
        for i in range(m):
            x, y = input().split()
            x, y = map(int, [x,y])
            G[x-1] += [y-1]
        
    
        for i in range(n):
            if i not in vis:
                if self.buscaProfundidade(G, i):
                    return 1
        return 0

testes = input()
d1 = Documentos(int(testes))

for i in range(d1.testes):
    vis = {}
    n, m = input().split()
    n, m = map(int, [n,m])
    caso = d1.instancia(n,m)

    if(caso == 1 ):
        print("SIM")
    else:
        print("NAO")
