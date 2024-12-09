saldo = 1000
saque = 200
limite = 100

saldo >= saque
saque <= limite

# Operador E (and). Ambas devem ser verdadeiras
saldo >= saque and saque <= limite


# Operador OU (or). Apenas uma deve ser verdadeira
saldo >= saque or saque <= limite

# Exemplos mais rápidos AND e OR
print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)


# Operador Negação. 
contatos_emergencia = [] # Esta é uma lista vazia, listas vazia são consideradas falsas em Python

not contatos_emergencia # Por conta da lista ser vazia, o not vai retornar como verdadeira, já que a lista é falsa

not 1000 > 1500

not "saque 1500" # Strings preenchidas são consideradas verdadeiras, por isso vai retornar como falso

not "" # Strings vazias são consideradas falsas, por isso vai retornar como verdadeira


# Parênteses, servem para delimitar a precedência
saldo = 1000
saque = 200
limite2 = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print (exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)


conta_normal_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_saldo_suficiente or conta_especial_saldo_suficiente
print (exp_3)