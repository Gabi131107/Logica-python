produto = input("Digite o nome do produto: ")
estoque = int(input("Digite o estoque disponível: "))
quantidade = int(input("Digite a quantidade solicitada: "))

if quantidade <= estoque:
    print(f"Produto: {produto}")
    print("Pedido pode ser atendido")
else:
    print(f"Produto: {produto}")
    print("Estoque insuficiente")