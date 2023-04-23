# Questão 14 - Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
# Em seguida, verifique se o número 3 está presente no conjunto.

conjunto = set()

for i in range(5):
    valor = int(input('Valor: '))
    conjunto.add(valor)
    
if 3 in conjunto: print('3 está no conjunto.')
else: print('3 não está no conjunto.')
    