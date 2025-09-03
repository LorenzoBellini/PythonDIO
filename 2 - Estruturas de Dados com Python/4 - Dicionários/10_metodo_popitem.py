contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
}
print(contatos)

print("----- Após o update -----")

contatos.popitem()  # Remove o último item adicionado
print(contatos)
