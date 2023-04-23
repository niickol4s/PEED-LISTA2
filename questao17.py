# Questão 17 - Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
# Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.

tupla = tuple()

for i in range(3):
    nome = input('Nome: ')
    tupla.__add__ += (nome,)

print(tupla)
print(tupla.count('Maria'))
