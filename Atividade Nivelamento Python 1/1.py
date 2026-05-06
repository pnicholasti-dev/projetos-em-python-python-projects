nconta = int(input("Informe o número da sua conta: "))
saldo = int(input("Informe o seu saldo: "))
crédito = int(input("Informe o seu crédito: "))
débito = int(input("Informe o seu débito: "))
saldo_atual= saldo - débito + crédito
print("Saldo atual: ", saldo_atual)
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
