class Veiuculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'


class Motocicleta(Veiuculo):
    pass


class Carro(Veiuculo):
    pass


class Caminhao(Veiuculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"Estou" if self.carregado else "Não estou"} carregado')


moto = Motocicleta("Preta", "ABC1234", 2)

carro = Carro("Vermelho", "XYZ5678", 4)

caminhao = Caminhao("Azul", "DEF9012", 8, True)

print(carro)
print(moto)
print(caminhao)
