contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
}


# Exemplo do método copy() em dicionários em Python
copia = contatos.copy()
copia["lorenzo@gmail.com"] = {"nome": "Lo"}

print(contatos["lorenzo@gmail.com"])
print(copia["lorenzo@gmail.com"])

# O método copy() cria uma cópia rasa (shallow copy) do dicionário original.
# Modificações na cópia não afetam o dicionário original.
