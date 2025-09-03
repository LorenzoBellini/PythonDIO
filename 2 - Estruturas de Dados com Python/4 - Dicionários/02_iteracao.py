contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
    "giulia@gmail.com": {"nome": "Giulia", "telefone": "88888-8888"},
    "anderson@gmail.com": {"nome": "Anderson", "telefone": "77777-7777"},
    "mayra@gmail.com": {"nome": "Mayra", "telefone": "66666-6666"},
}

# Dois exemplos de iteração em dicionários em Python

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)
