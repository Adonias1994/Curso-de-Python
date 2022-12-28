import os
os.system('cls')

# Exemplo de matriz
carros = [
    ['Modelo', 'HRV'],
    ['Fabricante', 'Honda'],
    ['Ano', 2016]
]
carros[2][1] = 2022 # Exemplo de alteração de dados de determinado índice
carros.append(['Cor', 'Branco']) # append adiciona elementos em nossa matriz
carros[3][1] = 'Prata' # Alteração de dado em elemento que foi adicionado posteriormente

print('\nAbaixo segue alguns exemplos de matrizes:.\n')
for l, c in carros: # l para linha e c para coluna
    print('---> ' + l + ': ' + str(c) + '.')
print('\nNão deixe de abrir o código e acompanhar com os comentários.\n')
