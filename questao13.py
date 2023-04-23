# Questão 13 - Crie um dicionário vazio. 
# Peça para o usuário digitar as chaves e os valores desse dicionário. 
# Em seguida, verifique se a chave 'profissão' está presente no dicionário

tam = int(input('Tamanho: '))
dicionario = dict()

for i in range(tam):
    chave = input('Chave: ')
    valor = input('Valor: ')
    dicionario[chave] = valor
print(dicionario)

if 'profissão' in dicionario: print('Chave "profissão" está presente.')
else: print('Chave "profissão" não está presente.')