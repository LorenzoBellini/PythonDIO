contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
}

contatos.setdefault("nome", "Luigi")  # Não altera, pois já existe

print(contatos)

print("----- Após o update -----")

contatos.setdefault("idade", 25)  # Adiciona, pois não existe

print(contatos)
