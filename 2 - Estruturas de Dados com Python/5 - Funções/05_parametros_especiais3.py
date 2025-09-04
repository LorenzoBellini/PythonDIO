def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Civic", 2024, "ABC2D34", marca="Honda", motor="2.0", combustivel="Gasolina")  # Correto
print("=" * 100)

criar_carro(modelo="Civic", ano=1999, placa="XYZ9Z99", marca="Honda", motor="2.0", combustivel="Gasolina")  # Errado, pois os 3 primeiros parametros são apenas posicionais