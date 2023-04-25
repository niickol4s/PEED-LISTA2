# Questão 2 - Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
# Em seguida, peça para o usuário escolher um dos nomes e substituir 
# esse nome por outro nome que ele também deve digitar.

listaNome = []

def inserir(nome):
    listaNome.append(nome)
    return listaNome

def substituir(nome):
    listaNome.remove(nome)
    novoNome = input('Novo nome: ')
    listaNome.append(novoNome)
    return listaNome

for i in range(3):
    inserir(input('Nome: '))
    
tuplaNome = tuple(listaNome)
nomeSubst = None

while True:
    nomeSubst = input('Substituir nome: ')
    
    if nomeSubst in tuplaNome:
        break
    else:
        print('Nome não inserido.')

tuplaNome = tuple(substituir(nomeSubst))
print(tuplaNome)
