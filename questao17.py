# Questão 17 - Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
# Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.

lista = list()

for i in range(3):
    lista.append(input('Nome: '))

tupla = tuple(lista)

print(tupla)
print(tupla.count('Maria'))
