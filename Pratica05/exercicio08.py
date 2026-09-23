renda = float(input("Digite a renda: "))
score = int(input("Digite o score: "))

renda_minima = float(input("Digite a renda mínima estabelecida: "))
score_minimo = int(input("Digite o score mínimo estabelecido: "))

if renda >= renda_minima and score >= score_minimo:
    print("Crédito aprovado")
else:
    print("Crédito não aprovado")