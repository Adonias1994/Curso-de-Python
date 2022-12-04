'''
Aula sobre coleção list
Diversos exemplos digitados para fixação
'''
#coding: utf-8
one = ['Luffy', 'Zoro', 'Sanji'] #Exemplo de lista
naruto = ['Naruto', 'Sasuke', 'Sakura']
dragonball = ['Vegeta', 'Kakaroto', 'Broly']
print(one) #Imprime a lista completa
print(one[0]) #Imprime o primeiro elemento
print(one[1]) #Imprime o segundo elemento
print(one[2]) #Imprime o terceiro elemento
print(one[-1]) #Imprime o terceiro elemento
print(one[-2]) #Imprime o segundo elemento
print(one[-3]) #Imprime o primeiro elemento
one[2] = 'Nami' #Com isso substituimos o terceiro elemento
print(one[2])
print(one)
one.append('Sanji') #Esse método adiciona novos itens a lista de elementos
print(one)
print(str(len(one))) #Imprime a quantidade da lista
one.remove('Nami') #Realiza a remoção da lista
print(one)
print(str(len(one)) + ' - Lista atualizada sem o elemento 3')
one.pop() #Remove o último elemento de nossa lista
del one[0] #Remove o elemento com o número informado
print(one)
one.clear()
print(one)
one.append('Luffy')
one.append('Zoro')
one.append('Sanji')
animes = list(one + naruto) #Adiciona elementos de uma lista a outra
print(animes)
animes3 = animes + dragonball #Essa é outra forma de juntar listas
print(animes3)
print('\nA quantidade de elementos na lista animes3 é ' + str(len(animes3)) + '.\n')
