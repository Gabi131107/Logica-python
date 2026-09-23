total = float(input("Digite o valor da compra: "))
cliente_vip = input("O cliente é VIP? (sim/não): ")
cupom = input("O cliente possui cupom? (sim/não): ")

if total >= 200 and (cliente_vip == "sim" or cupom == "sim"):
    print("Desconto promocional concedido")
else:
    print("Desconto promocional não concedido")