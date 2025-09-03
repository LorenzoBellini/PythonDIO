contatos = {
    "lorenzo@gmail.com": {"nome": "Lorenzo", "telefone": "99999-9999"},
}

print(contatos.fromkeys(["nome", "telefone"], "vazio"))

# O método fromkeys() cria um novo dicionário com as chaves fornecidas e atribui a elas um valor padrão.
# Se nenhum valor for fornecido, o padrão será None.
