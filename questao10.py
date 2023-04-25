# Questão 10 - Crie um grafo vazio. 
# Peça para o usuário digitar os vértices e as arestas desse grafo. 
# O usuário deve informar os pares de vértices que formam cada aresta. 
# Em seguida, peça para o usuário escolher uma das arestas e removê-la do grafo.

grafo = {}

qtdVertice = int(input('Quantidade de vétices: '))
for i in range(qtdVertice):
    vertice = input(f'{i + 1}º vértice: ')
    grafo[vertice] = []
    
qtdAresta = int(input('Quantidade de arestas: '))
for i in range(qtdAresta):
    origem, destino = input('Arestas: ').split()
    grafo[origem] = destino
    grafo[destino] = origem
print(grafo)

removerAresta = input('Remover aresta: ')
origem, destino = removerAresta.split()

if origem in grafo and destino in grafo:
    if destino in grafo[origem]:
        grafo[origem].remove(destino)
        grafo[destino].remove(origem)
        print(grafo)
    else:
        print('A aresta não foi inserida.')
else:
    print('Vértice não inserido.')
    