# Questão 12 - Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
# Em seguida, verifique se o nome 'Maria' está presente na tupla.

lista = list()

for i in range(3):
    lista.append(input('Nome: '))
    
tupla = tuple(lista)

print(tupla)

if 'Maria' in tupla: 
    print('Maria está na tupla.')
else: 
    print('Maria não está na tupla.')
