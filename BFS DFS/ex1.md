Utilize a classe base para grafos e insira um método para imprimir na tela o resultado da Busca em Largura em um grafo, a partir de um vértice v, fornecido como parâmetro.

O protótipo da função é BFS(s), onde

- s é o vértice de origem da BFS

#Teste 1

g = Graph(4)

g.addEdge(0, 1) 

g.addEdge(0, 2) 

g.addEdge(1, 2) 

g.addEdge(2, 0) 

g.addEdge(2, 3) 

g.addEdge(3, 3) 

g.BFS(2)

Saída:

2 0 3 1

#Teste 2

g = Graph(13)

g.addEdge(0,1)

g.addEdge(1, 2) 

g.addEdge(1, 3) 

g.addEdge(1, 4) 

g.addEdge(2, 5)

g.addEdge(2, 6) 

g.addEdge(4, 7) 

g.addEdge(4, 8) 

g.addEdge(5, 9) 

g.addEdge(5, 10) 

g.addEdge(7, 11) 

g.addEdge(7, 12)

g.BFS(0) 

Saída:

0 1 2 3 4 5 6 7 8 9 10 11 12