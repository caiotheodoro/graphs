Utilizando a classe criada anteriormente, escreva uma função para imprimir na tela o resultado da Busca em Profundidade em um grafo, a partir de um vértice inicial v, fornecido como  parâmetro

O protótipo da função é DFS(s), onde

s é o vértice de origem da DFS

OBS:

(1) é possível e indicado que vc crie funções auxiliares para sua resposta.

(2) selecione os vértices em ordem crescente de valor



#Teste 1

g = Graph(4) 

g.addEdge(0, 1) 

g.addEdge(0, 2) 

g.addEdge(1, 2) 

g.addEdge(2, 0) 

g.addEdge(2, 3) 

g.addEdge(3, 3) 

g.DFS(2) 

Saída: 

2 0 1 3

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

g.DFS(0) 

Saída:

0 1 2 5 9 10 6 3 4 7 11 12 8