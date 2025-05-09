# [] -> parentes retos
# () -> parenteses
# {} -> chavetas

numeros = [1, 2, 3, 4, 5]
print(numeros)

cidades = list(('Porto', 'Lisboa', 'Vila Real', 'Braga'))
print(cidades)

# random_list = ['José', 2, True]
# print(random_list)

# Obter elementos da Lista
print(cidades[0])
print(cidades[-1])
print(cidades[-2])
print()
print(len(cidades))
print(cidades[len(cidades) - 1])

# Adicionar elementos na lista
cidades.append('Luanda')
print(cidades)

cidades.remove('Luanda')
print(cidades)

cidades.insert(2, 'Bragança')
print(cidades)

cidades[4] = "Viana de Castelo"
print(cidades)

cidades.pop()
print(cidades)

cidades.reverse()
# print(cidades._____)
