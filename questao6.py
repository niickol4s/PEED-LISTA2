# Questão 6 - Crie uma lista vazia e peça para o usuário digitar 10 números. 
# Em seguida, adicione esses números à lista utilizando um loop for.

lista = list()

for i in range(10): lista.append(int(input(f'{i + 1}º valor: ')))
print(lista)
    