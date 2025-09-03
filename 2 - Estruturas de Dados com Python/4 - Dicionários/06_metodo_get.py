contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
}

print(contatos.get("chave"))  # None
print(contatos.get("chave", {}))  # {}
print(contatos.get("lorenzo@gmail.com", {}))  # {'nome': 'Lorenzo', 'telefone': '99999-9999'}
