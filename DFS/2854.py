pessoas = []
familias = []


class Arvore:
    def __init__(self, qtdPessoas, qtd):
        self.qtdPessoas = qtdPessoas
        self.insereRelacao = []
        self.familia = {}
        self.qtd = qtd
        for i in range(int(qtdPessoas)):
            pessoas.append(int(0))
        return

    def insereLaco(self, string):
        var = string.split()
        self.insereRelacao.append((var[0], var[2]))

    def insereFamilias(self):

        for item in self.insereRelacao:
            if item[0] in self.familia:
                self.familia[item[0]].append(item[1])
            else:
                self.familia[item[0]] = [item[1]]

            if item[1] in self.familia:
                self.familia[item[1]].append(item[0])
            else:
                self.familia[item[1]] = [item[0]]

    def DFS(self, node, visited_nodes):
        if node not in visited_nodes:
            visited_nodes.append(node)

            for adjacent_node in self.familia[node]:
                self.DFS(adjacent_node, visited_nodes)

    def qtdFamilias(self):
        contador = 0
        visitado = []
        for item in self.familia:
            if item not in visitado:
                contador += 1
                self.DFS(item, visitado)
        return contador


contador = 0

x, y = input().split()
x, y = map(int, [x, y])

a1 = Arvore(x, y)
for i in range(y):
    a1.insereLaco(input())

a1.insereFamilias()
contador = a1.qtdFamilias()


print(contador)
