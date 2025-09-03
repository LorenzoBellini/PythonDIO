contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
    "giulia@gmail.com": {"nome": "Giulia", "telefone": "88888-8888"},
    "anderson@gmail.com": {"nome": "Anderson", "telefone": "77777-7777"},
    "mayra@gmail.com": {"nome": "Mayra", "telefone": "66666-6666"},
}

print("lorenzo@gmail.com" in contatos)  # True
print("matheus@gmail.com" in contatos)  # False
print("idade" in contatos["lorenzo@gmail.com"])  # False
print("telefone" in contatos["mayra@gmail.com"])  # True
