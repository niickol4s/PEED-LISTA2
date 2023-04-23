# Questão 4 - Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
# Em seguida, peça para o usuário escolher um dos números e removê-lo do conjunto.

conjunto = set()

for i in range(5): conjunto.add(int(input('Valor: ')))
print(conjunto)

removerValor = int(input('Remover: '))

if removerValor in conjunto: conjunto.remove(removerValor)
else: print('Valor não inserido.')

print(conjunto)
    