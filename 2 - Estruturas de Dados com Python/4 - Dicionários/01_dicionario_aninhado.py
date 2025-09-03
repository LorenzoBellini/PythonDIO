# Exemplo de dicionário aninhado em Python

contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
    "giulia@gmail.com": {"nome": "Giulia", "telefone": "88888-8888"},
    "anderson@gmail.com": {"nome": "Anderson", "telefone": "77777-7777"},
    "mayra@gmail.com": {"nome": "Mayra", "telefone": "66666-6666"},
}

print(contatos["mayra@gmail.com"]["telefone"])  # Acessa o telefone de Mayra. 66666-6666
