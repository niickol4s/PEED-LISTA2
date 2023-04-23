# Questão 7 - Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
# Em seguida, retorne o primeiro elemento da tupla.

tupla = tuple()

for i in range(5):
    valor = int(input('Valor: '))
    tupla += (valor,)

print(f'Valor do primeiro índice: {tupla[0]}')
