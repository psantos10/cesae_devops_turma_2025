# import datetime
from datetime import date
# # import time
from time import time

hoje = date.today()
print(hoje)
hora = time()
print(hora)

# python3 -m venv path/to/venv
# source path/to/venv/bin/activate
# python3 -m pip install xyz

print()

import camely

texto = "este_texto_esta_em_snake_case"
print(camely.convert(texto))

print()

from validar import validar_email

email = "teste@exemplo.com"
if validar_email(email):
  print("O email é válido")
else:
  print("O email é inválido")
