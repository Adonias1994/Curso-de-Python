#TIPOS NUMÉRICOS, RANDOM E OPERAÇÕES DE CASTING
#utf-8
import random #Gera números aleatórios
num_i = 10 #Inteiro
num_f = 5.2 #Flutuante
num_c = 1j #Complexo
a = num_i
print('Valor: ' + str(a) + ' - Tipo: ' + str(type(a))) #Conversão de inteiro para string (Casting)
b = num_f
print('Valor: ' + str(b) + ' - Tipo: ' + str(type(b))) #Conversão de flutuante para string (Casting)
c = num_c
print('Valor: ' + str(c) + ' - Tipo: ' + str(type(c))) #Conversão de complexo para string (Casting)
num_r = [
    random.randrange(0, 100), #Gera o primeiro número aleatório entre 0 e 100
    random.randrange(0, 100), #Gera o segundo número aleatório entre 0 e 100
    random.randrange(0, 100), #Gera o terceiro número aleatório entre 0 e 100
    ]
d = num_r
print('Valor: ' + str(d) + ' - Tipo: ' + str(type(d))) #num_r é um array, logo o tipo de d é lista, não inteiro
