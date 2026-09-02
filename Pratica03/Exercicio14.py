produto = input("Nome do produto: ")
preco = float(input("Preço unitário: "))
quantidade = int(input("Quantidade: "))

total = preco * quantidade

print("===== COMPRA =====")
print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco}")
print(f"Quantidade: {quantidade}")
print(f"Valor total: R$ {total}")
