# Questão 1 - Peça para o usuário digitar 5 números e crie uma lista com esses números. 
# Em seguida, peça para o usuário digitar mais um número e adicione esse número à lista.

lista = list()

for i in range(5): lista.append((int(input(f'{i + 1}º valor: '))))

lista.append(int(input('Insira o 6º valor: ')))
print(lista)