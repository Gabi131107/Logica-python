produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))
cliente_vip = input("O cliente é VIP? (sim/não): ")
cupom = input("Possui cupom? (sim/não): ")

total = preco * quantidade

if total >= 200 and (cliente_vip == "sim" or cupom == "sim"):
    desconto = True
    print("Desconto promocional concedido")
else:
    desconto = False
    print("Desconto promocional não concedido")

if total >= 200 or cliente_vip == "sim":
    frete_gratis = True
    print("Frete grátis")
else:
    frete_gratis = False
    print("Frete não é grátis")

print(f"Produto: {produto}")
print(f"Total da compra: R$ {total:.2f}")