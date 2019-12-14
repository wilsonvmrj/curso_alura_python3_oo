from conta import Conta

conta = Conta(123,"Wilson",500.0,1000.0)

print("Saldo {}".format(conta.saldo))

print(conta.limite)
print(conta.titular )
conta.limite = 2000
print(conta.limite )