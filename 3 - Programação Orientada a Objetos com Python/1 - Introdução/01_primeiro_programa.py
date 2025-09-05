'''
João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas
Crie um programa aonde João informe:
Cor, Modelo, Ano e Valor da bicicleta vendida
Uma bicicleta pode: Buzinar, parar e correr. Adicione esses comportamentos
'''


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor,):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Biiiiii")

    def parar(self):
        print("Parando bike")
        print("Bike parada")

    def correr(self):
        print("Vrummmm\n" * 3)

    # def __str__(self):
    #     return f"{self.cor} {self.modelo} {self.ano} {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
print(b1)

print("-" * 60)

b2 = Bicicleta("Preta", "Monark", 2020, 450)
print(b2)
