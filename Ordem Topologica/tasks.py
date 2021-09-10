loop = True
from collections import defaultdict

class Documentos:
    def __init__(self, vertices):
        self.Vertices = vertices
        self.grafo = defaultdict(list)
   
        for i in range(vertices):
            self.grafo[i] = []
        return
    def addEdge(self,u,v): # adiciona aresta no inicio da lista
        self.grafo[u].insert(0,v)

        return

    def topologicalSortUtil(self,visited,stack,v):
        # marca o nó atual como visitado.
        visited[v] = True
        
        # itera todos os vertices adjacentes ao v
        for i in self.grafo[v]:
                    # caso o vertice não tenha sido visitado
            if visited[i] == False:
                self.topologicalSortUtil(visited,stack,i)
                # Insere o nó atual na pilha
        stack.insert(0,v)
        

    def topologicalSort(self):
        #marca nao visitados
        visited = [False] * self.Vertices
       
          
        stack =[]
        # chama a funçao auxiliar recursive para guardar
        # a orddenaçao Topologica na pilha
        for i in range(self.Vertices):
            if visited[i] == False:
                self.topologicalSortUtil(visited,stack,i) 
                #stack
        for i in stack: #imprime a ordem topologica
            print(i+1,end=" ") 
        print() 



while (loop): 
    vertices, testes = input().split()
    vertices, testes = map(int, [vertices, testes])
    if (vertices == 0 and testes == 0): # sai do loop
        loop = False
        break
    v1 = Documentos(vertices)
    for i in range(testes):
        n, m = input().split() # n = vertice m = aresta
        n, m = map(int, [n,m]) #transforma em inteiro
        v1.addEdge(n-1,m-1) 

    v1.topologicalSort()
