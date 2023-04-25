# Questão 19 - Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
# Em seguida, verifique quantos elementos estão no conjunto.

conjunto = set()

for i in range(5): 
    conjunto.add(int(input('Valor: ')))
print(f'Total: {len(conjunto)}')
