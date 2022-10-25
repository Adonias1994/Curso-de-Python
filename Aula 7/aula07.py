#coding: utf-8
curso = 'Curso de Python'
canal = 'CFB Cursos'

#res é resposta
res1 = 'Python\n' in curso #Consulta se a palavra está na variável
print(res1)
res2 = 'Python\n' not in curso #Consulta se a palavra não está na variável
print(res2)
res3 = curso + ' do canal ' + canal + '\n' #Exemplo de concatenação
print(res3)

#Exemplo de casting
cidade1 = 'Paulista'
dia1 = '24'
mes1 = 'Outubro'
ano1 = '2022'
data1 = cidade1 + ', ' + str(dia1) + ' de ' + mes1 + ' de ' + str(ano1) + '.\n'
print(data1)

#Método format
cidade2 = 'Paulista'
dia2 = '24'
mes2 = 'Outubro'
ano2 = '2022'
data2 = '{}, {} de {} de {}.\n'
print(data2.format(cidade2, dia2, mes2, ano2))

#Caracteres de escape #ex é exemplo
ex1 = '\'Asplas simples(ver código e comentários)\'\n' #Aspas simples
print (ex1)
ex2 = '\"Asplas duplas(ver código e comentários)\"\n' #Aspas duplas
print (ex2)
ex3 = '\nQuebra de linha(ver código e comentários)\n' #Quebra de linha
print (ex3)
ex4 = '\rEsse serve para especificar como estivessimos pressionando Enter(ver código e comentários)\n' #Enter pressionado
print (ex4)
ex5 = '\tTabulação(ver código e comentários)\n' #Como se tivessemos dado um Tab
print (ex5)
ex6 = '\bBack Space(ver código e comentários)\n' #Como se tivessemos dado um back space
print (ex6)