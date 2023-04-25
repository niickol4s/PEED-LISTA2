# Questão 7 - Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
# Em seguida, retorne o primeiro elemento da tupla.

lista = list()

for i in range(5):
    lista.append(int(input('Valor: ')))
    
tupla = tuple(lista)

print(f'Valor do primeiro índice: {tupla[0]}')
