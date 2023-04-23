# Questão 11 - Crie uma lista vazia e peça para o usuário digitar 10 números. 
# Em seguida, retorne os elementos de índice par da lista.

lista = list()

for i in range(10): lista.append(int(input(f'{i + 1}º valor: ')))
for i in range(0, 10, 2): print(f'Valores na posição par: {lista[i]}')
