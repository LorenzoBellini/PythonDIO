conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print (conjunto_a.issuperset(conjunto_b)) # False, nem todos os elementos de B estão em A
print (conjunto_b.issuperset(conjunto_a)) # True, todos os elementos de A estão em B