def salvar_carro(marca, modelo, ano, placa):
    # Simula o salvamento de um carro em um banco de dados
    print(f"Carro salvo com sucesso! Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Placa: {placa}")


# Chamando a função com argumentos nomeados
salvar_carro(marca="Toyota", modelo="Corolla", ano=2020, placa="ABC-1234")


# Outra maneira de chamar os argumentos (podem ser chamados fora de ordem)
salvar_carro(modelo="Civic", marca="Honda", placa="XYZ-5678", ano=2019)


# Mais uma maneira de chamar os argumentos usando um dicionário e o operador **
salvar_carro(**{"marca": "Volkswagen", "modelo": "Golf", "ano": 2018, "placa": "DEF-9012"})
