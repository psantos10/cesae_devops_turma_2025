menor_de_idade = 16
maior_de_idade = 25
filho_de_marcelo = False

if menor_de_idade >= 18:
  print(f"Com {menor_de_idade} anos podes frequentar esta discoteca!")
elif menor_de_idade >= 16 and filho_de_marcelo:
  print(f"Opa... É o filho do chefe. Ninguém mexe")
else:
  print(f"Lamentamos. Mas com {menor_de_idade} não podes frequentar esta discoteca!")

print()

numeros = [4, 8, 10]
if 18 in numeros:
  print("Encontrei o número oito")
else:
  print("Oops! Não encontrei o número que busca")


