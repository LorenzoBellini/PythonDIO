nome = "Lorenzo"
idade = 24
profissao = "Estudante"
linguagem = "Python"

pessoa = {"nome" : "Lorenzo", "idade" : "24", "profissao" : "Estudante", "linguagem" : "Python" }

print ("Olá, me chamo {}. Tenho {} anos de idade, atuo como {} e estou fazendo um urso de {}".format(nome, idade, profissao, linguagem))

print ("Olá, me chamo {3}. Tenho {2} anos de idade, atuo como {1} e estou fazendo um urso de {0}".format(linguagem, profissao, idade, nome))

print ("Olá, me chamo {nome}. Tenho {idade} anos de idade, atuo como {profissao} e estou fazendo um urso de {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print ("Olá, me chamo {nome}. Tenho {idade} anos de idade, atuo como {profissao} e estou fazendo um urso de {linguagem}".format(**pessoa))