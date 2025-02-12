numeros = set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4} Os valores 1 e 3 estão duplicados, o construtor set vai remover as duplicidades
print (numeros)

letras = set("abacaxi") # {"b", "a", "c", "x", "i"} O construtor set não garante a ordem dos elementos, ele considera letras maiúsculas e minúsculas diferentes, se tiver um a e um A ele vai incluir ambos
print (letras)

carros = set(("Palio", "Gol", "Celta", "Palio")) # {"Gol", "Celta", "Palio"}
print (carros)

linguagens = {"Python", "Java", "Python"} # Conjuntos também podem ser feitos utilizando chaves {}
print (linguagens)