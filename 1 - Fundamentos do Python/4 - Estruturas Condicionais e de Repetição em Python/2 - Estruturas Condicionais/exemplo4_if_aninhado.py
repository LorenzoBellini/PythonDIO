# Exemplo If Aninhado
# Definição inicial de variáveis
saldo = 1000
cheque_especial = 500  # Valor do cheque especial
conta_normal = True    # Indica se é uma conta normal
conta_universitaria = False  # Indica se é uma conta universitária

# Entrada do usuário
try:
    saque = float(input("Digite o quanto quer sacar: "))  # Conversão para número
    if saque <= 0:
        print("O valor do saque deve ser maior que zero.")
    else:
        # Verificação da conta
        if conta_normal:
            if saldo >= saque:
                print("Saque realizado com sucesso!")
            elif saque <= (saldo + cheque_especial):
                print("Saque realizado com uso do cheque especial!")
            else:
                print("Saldo insuficiente, mesmo com cheque especial.")
        elif conta_universitaria:
            if saldo >= saque:
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Tipo de conta não identificado.")
except ValueError:
    print("Por favor, insira um valor numérico válido.")
