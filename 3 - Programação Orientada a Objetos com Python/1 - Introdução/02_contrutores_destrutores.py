# __init__ é um método construtor em Python (ou inicializador)

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a Classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo instancia de classe")

    def falar(self):
        print("Au Au")


def criar_cachorro():
    c = Cachorro("Ambrosia", "Preto", False)
    print(c.nome)


criar_cachorro()
# __del__ é um método destrutor em Python executado quando o objeto é destruído
# Sempre executado ao final do programa ou quando o objeto é deletado
# Para forçar a remoção de um objeto, use a função del
