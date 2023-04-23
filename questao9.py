# Questão 9 - Peça para o usuário digitar 10 números e crie um conjunto com esses números. 
# Em seguida, remova todos os números pares do conjunto.

conjunto = set()

for i in range(10): 
    valor = int(input('Valor: '))
    conjunto.add(valor)
    if valor % 2 == 0: conjunto.remove(valor)
        
print(conjunto)
