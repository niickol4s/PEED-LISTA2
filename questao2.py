# Questão 2 - Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
# Em seguida, peça para o usuário escolher um dos nomes e substituir 
# esse nome por outro nome que ele também deve digitar.

listaNome = []

def inserir(nome):
    tupla = (nome)
    listaNome.append(nome)
    return listaNome

def substituir(nome):
    buscarNome = input('Buscar nome: ')
    listaNome.remove(buscarNome)
    novoNome = input('Novo nome: ')
    listaNome.append(novoNome)
    return listaNome

for i in range(3): listaNome.append(input('Nome: '))
print(listaNome)

substituir(listaNome)
print(listaNome)
