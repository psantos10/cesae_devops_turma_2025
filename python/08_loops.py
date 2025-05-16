residentes_no_porto = [
  {'nome': 'Maria', 'idade': 19},
  {'nome': 'Felipe', 'idade': 18},
  {'nome': 'José', 'idade': 21},
  {'nome': 'Paulo', 'idade': 16},
  {'nome': 'Magda', 'idade': 22},
]

for residente in residentes_no_porto:
  print(f'Cidadao do Porto: {residente['nome']}')

print()

for residente in residentes_no_porto:
  if residente['idade'] < 18:
    continue

  print(f'Cidadao do Porto: {residente['nome']}')

print()

for residente in residentes_no_porto:
  if residente['nome'] == "Paulo":
    print(f'Encontrei o: {residente['nome']}')
    break

for i in range(1, 11):
  print(i, end=", ")

print()


contagem = 0
while contagem < 10:
  print(f'Contagem atual: {contagem}')
  contagem += 1
