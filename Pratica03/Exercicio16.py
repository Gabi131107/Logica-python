preco = float(input("Preço: "))
desconto = float(input("Desconto em reais: "))

preco_final = preco - desconto

print("===== DESCONTO =====")
print(f"Preço original: R$ {preco}")
print(f"Desconto: R$ {desconto}")
print(f"Preço final: R$ {preco_final}")
