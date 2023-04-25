# Questão 8 - Crie um dicionário vazio. 
# Peça para o usuário digitar as chaves e os valores desse dicionário. 
# Em seguida, retorne o valor da chave 'idade'.

tam = int(input('Tamanho: '))
dicionario = dict()

for i in range(tam):
    chave = input('Chave: ')
    valor = input('Valor: ')
    dicionario[chave] = valor

if 'idade' in dicionario:
    print(f'Idade: {dicionario["idade"]}')
else:
    print('Idade não foi inserida.')
        
print(dicionario)
