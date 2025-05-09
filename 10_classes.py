# Classe
# Classe = Carro
# Object = Tesla

class Carro:
  def __init__(self, modelo):
    print(f"Criando o carro: {modelo}")

  def acelerar(self, kmph):
    return f"Vroooommmmm... acelerrando a {kmph}/Km por hora"


tesla = Carro("Tesla X")
print(tesla)

print(tesla.acelerar(100))
