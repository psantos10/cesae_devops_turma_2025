marta = {
  'nome': 'Marta',
  'idade': 19,
  'cidade': 'Porto'
}

print(marta)
print(marta['nome'])
print(marta.get('cidade'))

marta['idade'] = 20
print(marta)

marta['linguagem_favorita'] = 'Python'
print(marta)

marta.pop('linguagem_favorita')
print(marta)

marta.clear()
print(marta)

print()

residentes_no_porto = [
  {'nome': 'Marta', 'idade': 18, 'marcas_de_carro': ['BMW', 'Tesla']},
  {'nome': 'José', 'idade': 20},
  {'nome': 'Beatriz', 'idade': 22}
]
print(residentes_no_porto)

marta = residentes_no_porto[0]
print(marta['nome'])

print(residentes_no_porto[0]['nome'])
