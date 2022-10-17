#coding: utf-8
#String - Parte 1
curso = ' Curso de Python ' #Uma variável trata-se de uma cadeia de caractéres
print(curso[10])
print('Tamanho: ' + str(len(curso))) #Retorna o tamanho da variável
print(curso.strip()) #Remove os espaços no início e no fim da variável
print(curso.lower()) #Converte para minúsculos
print(curso.strip().lower()) #É possível utilizar as duas
print(curso.strip().upper()) #A função upper converte para maiúsculos
print(curso.replace('Python', 'Python 3').strip()) #replace substitui informações na String
a = curso.split(' ') #Especificado espaços para o split realizar um corte
print(a[1]) #Depois do array especificado o que foi determinado como split, o array escolhido é mostrado antes do corte
