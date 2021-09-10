Utilizando a classe criada anteriormente como base, insira um método para retornar a quantidade de vértices em um certo nível da Busca em Largura.

A assinatura desse método é qtVertices(s, L), onde 

s é o vértice inicial da busca em largura,

L é o nível que se deseja saber.

#Teste 1

g = Graph(6)

g.addEdge(0, 1)

g.addEdge(0, 2) 

g.addEdge(1, 3) 

g.addEdge(2, 4) 

g.addEdge(2, 5)

print(g.qtVertices(0,2)) 

Saída:

3

#Teste 2

g = Graph(7)

g.addEdge(0,1)

g.addEdge(0,2)

g.addEdge(1,3)

g.addEdge(1,4) 

g.addEdge(1,5)

g.addEdge(2,6)

print(g.qtVertices(0,2))

Saída:

4