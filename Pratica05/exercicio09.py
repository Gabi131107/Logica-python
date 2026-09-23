total = float(input("Digite o valor da compra: "))
cliente_vip = input("O cliente é VIP? (sim/não): ")

if total >= 200 or cliente_vip == "sim":
    print("Frete grátis")
else:
    print("Frete não é grátis")