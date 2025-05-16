class Conta:
  numero_de_conta = 0

  def __init__(self, titular, numero, saldo=0):
    self.titular = titular
    self.numero = numero
    self.saldo = saldo
    Conta.numero_de_conta += 1

  def info(self):
    print(f"Titular: {self.titular}")
    print(f"Número: {self.numero}")
    print(f"Saldo atual: {self.saldo} EUR")

  def depositar(self, valor):
    self.saldo += valor

  def transferir(self, valor: int, conta_destino: "Conta"):
    self.saldo -= valor
    conta_destino.saldo += valor

  def levantar(self, valor):
    self.saldo -= valor


class ContaPrazo(Conta):
  def __init__(self, titular, numero, saldo=0):
    super().__init__(titular, numero, saldo)

  def info(self):
    print("Conta a Prazo:")
    super().info()


conta_prazo = ContaPrazo("Moita", "12345")
conta_prazo.info()
print()
cc = Conta("Lidia", "56789")
cc.info()

print()
print(f"Número total de contas: {Conta.numero_de_conta}")


# conta_maria = Conta("Maria", "12345")
# conta_maria.info()
# conta_maria.depositar(850)
# conta_maria.info()
# print()
# nome_joao = "João"
# conta_joao = Conta(nome_joao, "67890", 0)
# conta_joao.info()

# print()

# conta_maria.transferir(150, conta_joao)
# conta_maria.info()
# conta_joao.info()


# ContaCorrente
# ContaPrazo
# ....
