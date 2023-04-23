# Questão 8 - Crie um dicionário vazio. 
# Peça para o usuário digitar as chaves e os valores desse dicionário. 
# Em seguida, retorne o valor da chave 'idade'.

tam = int(input('Tamanho: '))
dicionario = dict()

for i in range(tam):
    chave = input('Nome: ')
    valor = int(input('Idade: '))
    dicionario[chave] = valor
print(dicionario)
print(f'Idades: {dicionario.values()}')
