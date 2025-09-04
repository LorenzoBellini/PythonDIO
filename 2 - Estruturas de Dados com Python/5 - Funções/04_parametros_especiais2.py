def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(modelo="Civic", ano=2024, placa="ABC2D34", marca="Honda", motor="2.0", combustivel="Gasolina")  # Correto

print("=" * 100)

criar_carro("Civic", 2024, "ABC2D34", "Honda", "2.0", "Gasolina")  # Errado, pois todos os parametros são apenas nomeados
