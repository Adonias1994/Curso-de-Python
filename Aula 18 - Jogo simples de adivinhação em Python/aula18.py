import random
import os

erros = 0
sorteado = random.randrange(0, 100)
jogador = int(input('Digite um número: '))
while(sorteado!= jogador):
    os.system('cls')
    if(sorteado > jogador):
        print('O número sorteado é maior que o que você digitou.')
    elif(sorteado < jogador):
        print('O número sorteado é menor do que o que você digitou.')
    erros += 1
    jogador = int(input('Digite um número: '))
print('Número ' + str(jogador) + ', você acertou em ' + str(erros + 1) + ' tentativas.')
