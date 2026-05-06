maça = float(input("Digite a quantidade de maçãs: "))
if maça <= 12:
    preço = 1.30
else:
    preço = 1
custo_total = maça*preço
print("Custo total será de: ", custo_total)

forma = input("Forma de pagamento (dinheiro/cartao): ")
if forma == "dinheiro":
    pago = float(input("Valor pago: R$ "))
    if pago < custo_total:
        print("Pagamento inválido")
    else:
        troco = pago - custo_total
        print("Troco: R$ ", troco)
else:
    print("Pagamento realizado no cartão")
