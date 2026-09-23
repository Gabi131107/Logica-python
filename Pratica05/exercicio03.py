orcamento = float(input("Digite o orçamento disponível: "))
gasto = float(input("Digite o gasto realizado: "))

saldo = orcamento - gasto

print(f"Saldo: R$ {saldo:.2f}")
print(gasto <= orcamento)