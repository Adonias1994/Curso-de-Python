'''
a = 5
b = 2
if a > b:
    print('\nVerdadeiro.\n')
else:
    print('\nFalso.\n')
'''
# Calculadora simples
v1 = int(input('\nDigite o valor de x: '))
o = input('Digite a operação desejada: ')
v2 = int(input('Agora o valor de y: '))
if o == '+':
    print('\nA soma de x e y é: ', v1 + v2, '\n')
elif o =='-':
    print('\nA subtração de x e y é: ', v1 - v2, '\n')
elif o =='*':
    print('\nA multiplicação de x e y é: ', v1 * v2, '\n')
elif o =='/':
    print('\nA divisão de x e y é: ', v1 // v2, '\n')
else:
    print('\nVocê digitou uma operação inválida.\n')

