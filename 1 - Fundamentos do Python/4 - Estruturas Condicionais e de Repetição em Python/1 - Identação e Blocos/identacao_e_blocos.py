# Exemplo de um bloco em Python

def sacar (valor):
    saldo = 500
    
    if saldo >= valor:
        print ("Valor sacado! Retire-o na boca do caixa.")
    
    print ("Obrigado por ser nosso cliente, tenha um ótimo dia!")

def depositar (valor):
    saldo = 500
    saldo += valor
    
sacar(1000)