# # cidades = ('Lisboa', 'Porto', 'Viana de Castelo')
# cidades = tuple(('Lisboa', 'Porto', 'Viana de Castelo'))
# print(cidades)

# paises = ('Angola')
# paises2 = ('Angola',)
# print(paises, type(paises))
# print(paises2, type(paises2))

# print(cidades[0])

# # cidades[0] = 'Braga'
# print(len(cidades))

# del cidades
# print(cidades)

# Sets

# numeros = (1, 2, 3, 3, 4)
# print(numeros)
numeros = {1, 2, 2, 3, 4, 5}
print(numeros)

numeros.add(8)
print(numeros)

numeros.clear()
print(numeros)

del numeros
print(numeros)
