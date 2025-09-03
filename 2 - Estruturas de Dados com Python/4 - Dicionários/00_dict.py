dados = {"nome": "Lorenzo", "idade": 25, "telefone": "11999999999"}

print(dados["nome"])  # Lorenzo
print(dados["idade"])  # 25
print(dados["telefone"])  # 11999999999

# Atualizando os dados por outros
dados["nome"] = "João"
dados["idade"] = 30
dados["telefone"] = "11988888888"

print(dados)  # {'nome': 'João', 'idade': 30, 'telefone': '11988888888'}
