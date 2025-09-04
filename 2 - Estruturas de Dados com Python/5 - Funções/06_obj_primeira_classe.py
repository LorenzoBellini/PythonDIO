def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {resultado}")


exibir_resultado(5, 3, somar)
exibir_resultado(5, 3, multiplicar)

# Acima definimos uma função somar que recebe dois argumentos e retorna a soma deles.
# Também definimos uma função exibir_resultado que recebe dois números e uma função como argumentos.
# Dentro de exibir_resultado, chamamos a função passada como argumento com os dois números e exibimos o resultado.