cliente = input("Nome do cliente: ")
produto = input("Produto: ")
preco = float(input("Preço unitário: "))
quantidade = int(input("Quantidade: "))

total = preco * quantidade

print("========== PEDIDO ==========")
print(f"Cliente: {cliente}")
print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco}")
print(f"Quantidade: {quantidade}")
print(f"Total da compra: R$ {total}")
print("============================")
