#utf-8
var1 = 'Essa é uma variável global' #Variável global / Pode ser acessada de qualquer lugar do programa
def cn():
    var2 = 'Essa é uma variável local' #Variável local / Só pode ser chamada dentro do escopo
    print(var1)
    print(var2)
cn()
