def exibir_mensagem():
    print("Olá, mundo!")
    print("=" * 150)


def exibir_mensagem_2(nome):
    print(f'Seja bem vindo(a) {nome}!')
    print("=" * 150)


def exibir_mensagem_3(nome="Anônimo"):  # Parâmetro com valor padrão, caso nenhum valor seja passado na chamada da função o valor "Anônimo" será utilizado
    print(f'Seja bem vindo(a) {nome}!')
    print("=" * 150)


exibir_mensagem()

exibir_mensagem_2(nome="Lorenzo")  # Argumento nome recebe o valor "Lorenzo"

exibir_mensagem_3()

exibir_mensagem_3("Mayra")
