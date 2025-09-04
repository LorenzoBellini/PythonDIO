# Sobre parametros especiais em Python
# Segue exemplo de sintaxe

# def f(pos1,pos2, / pos_or_kw, *, kw1, kw2):
# pos1 e pos2 - apenas posicionais
# pos_or_kw - pode ser posicional ou nomeado
# kw1 e kw2 - apenas nomeados
# O que define isso é a barra (/) e o asterisco (*)
# A barra indica o fim dos parametros posicionais
# O asterisco indica o inicio dos parametros nomeados

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Civic", 2024, "ABC2D34", marca="Honda", motor="2.0", combustivel="Gasolina")  # Correto
print("=" * 100)

criar_carro("Civic", 2024, "ABC2D34", "Honda", "2.0", "Gasolina")  # Funciona, mas não é o ideal pois os 3 ultimos parametros são nomeados e deveriam ser chamados como nomeados
print("=" * 100)

criar_carro(modelo="Civic", ano=2024, placa="ABC2D34", marca="Honda", motor="2.0", combustivel="Gasolina")  # Errado, pois os 3 primeiros parametros são apenas posicionais
