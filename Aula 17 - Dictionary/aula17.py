import os
os.system('cls')

print('\nAlém de executar o algorítmo, abra ele para ver o código e os comentários.\n')

# Chave/Key -> Valor/Value
carro = {
    'Fabricante': 'Honda',
    'Modelo': 'HRV',
    'Ano': '2016',
    'Cor': 'Prata'
} # Exemplo de dicionário (coleção de dados sem ordem onde cada elemento possui um par chave/valor)

print(carro) # Imprime todos os valores
print('\n')
print(carro['Ano']) # Pode ser utilizado a chave para imprimir o conteúdo dela
print('\n')
carro['Cor'] = 'Preta' # Exemplo de como alterar algum elemento
print(carro)
for x in carro:
    print(x) # Imprime todas as chaves do dicionário
    print(carro[x]) # Imprime todos os valores das chaves contidas no dicionário
print('\n')
for c, v in carro.items():
    print(c + ': ' + v)
print('\n')

carro['Cambio'] = 'Automático' # Adicionando uma nova chave e valor
print(carro, '\n')

carro.pop('Cambio') # Remove
print(carro, '\n')

del carro['Cor'] # Também remove
print(carro, '\n')

carro.clear() # Limpa todo o dicionário
print(carro, '\n')
