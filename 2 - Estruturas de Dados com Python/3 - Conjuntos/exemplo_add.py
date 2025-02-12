sorteio = {1, 23}
print (sorteio) # {1, 23}

sorteio.add(25)
print (sorteio) # {1, 23, 25}

sorteio.add(42) 
print (sorteio) # {1, 23, 25, 42}

sorteio.add(25)
print (sorteio) # {1, 23, 25, 42} Como o 25 já tinha sido adicionado, não vai ser adicionado de novo, set não repete elementos