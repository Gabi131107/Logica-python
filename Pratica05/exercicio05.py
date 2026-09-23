nome = input("Digite o nome do vendedor: ")
meta = float(input("Digite a meta de vendas: "))
vendas = float(input("Digite as vendas realizadas: "))

percentual = vendas / meta * 100

print(f"Vendedor: {nome}")
print(f"Percentual atingido: {percentual:.2f}%")

if vendas >= meta:
    print("Meta atingida")
else:
    print("Meta ainda não atingida")