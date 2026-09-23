capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa mensal (%): "))
meses = int(input("Digite o número de meses: "))

juros = capital * taxa * meses / 100
montante = capital + juros

print(f"Juros: R$ {juros:.2f}")
print(f"Montante: R$ {montante:.2f}")