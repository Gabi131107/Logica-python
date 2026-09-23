saldo = float(input("Digite o saldo disponível: "))
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= saldo:
    print("Compra autorizada")
else:
    print("Saldo insuficiente")