# Questão 15 - Crie um grafo vazio. 
# Peça para o usuário digitar os vértices e as arestas desse grafo. 
# O usuário deve informar os pares de vértices que formam cada aresta. 
# Em seguida, verifique se a aresta ('A', 'C') está presente no grafo.

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

if 'A' in grafo and 'C' in grafo['A']:
    print('Aresta A C está no grafo.')
else:
    print('Aresta A C não está no grafo.')
