# Questão 12 - Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
# Em seguida, verifique se o nome 'Maria' está presente na tupla.

tuplaNome = ()

for i in range(3):
    nome = input('Nome: ')
    tuplaNome += (nome,)

print(tuplaNome)

if 'Maria' in tuplaNome: print('Maria está na tupla.')
else: print('Maria não está na tupla.')
