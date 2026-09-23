orcamento = float(input("Digite o orçamento: "))
gasto = float(input("Digite o gasto: "))

if gasto < orcamento:
    print("DENTRO")
elif gasto == orcamento:
    print("NO LIMITE")
else:
    print("ACIMA")