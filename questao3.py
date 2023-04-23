# Questão 3 - Crie um dicionário vazio. 
# Peça para o usuário digitar uma chave e um valor e adicione esses dados ao dicionário. 
# Em seguida, peça para o usuário adicionar mais uma chave e um valor 
# e adicione esses dados ao dicionário também

tam = int(input('Tamanho: '))
dicionario = dict()

for i in range(tam):
    chave = input(f'{i + 1}ª chave: ')
    valor = input(f'{i + 1}º valor: ')
    dicionario[chave] = valor

print(dicionario)
