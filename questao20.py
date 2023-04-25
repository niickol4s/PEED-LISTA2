# Questão 20 - Crie um grafo vazio. 
# Peça para o usuário digitar os vértices e as arestas desse grafo. 
# O usuário deve informar os pares de vértices que formam cada aresta. 
# Em seguida, mostre o grafo.

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
    