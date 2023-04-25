# Questão 18 - Crie um dicionário vazio. 
# Peça para o usuário digitar as chaves e os valores desse dicionário. 
# Em seguida, adicione uma nova chave e valor ao dicionário, 
# onde a chave é 'cidade' e o valor é a cidade em que o usuário nasceu.

tam = int(input('Tamanho: '))
dicionario = dict()

for i in range(tam):
    chave = input('Chave: ')
    valor = input('Valor: ')
    dicionario[chave] = valor

for i in range(1):
    chaveCidade = input('Cidade: ')
    valorLocal = input('Cidade que nasceu: ')
    dicionario[chaveCidade] = valorLocal

print(dicionario)
