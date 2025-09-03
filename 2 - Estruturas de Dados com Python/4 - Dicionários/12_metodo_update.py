contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
}
print(contatos)

print("----- Após o update -----")

contatos.update({"lorenzo@gmail.com": {"nome": "O cara", "telefone": "1234-5678"}})
print(contatos)
