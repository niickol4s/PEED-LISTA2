# Questão 16 - Peça para o usuário digitar 10 números e crie uma lista com esses números. 
# Em seguida, multiplique cada elemento da lista por 2 e crie uma nova lista com esses valores.

lista = list()
listaMult = list()

for i in range(10): lista.append((int(input('Valor: '))))
print(lista)

for valor in lista: listaMult.append(valor * 2)
print(listaMult)
