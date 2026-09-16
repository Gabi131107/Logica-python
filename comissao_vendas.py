
salario_fixo = float(input("Digite o salário fixo: "))
total_vendido = float(input("Digite o total vendido: "))
percentual_comissao = float(input("Digite o percentual de comissão (em %): "))

taxa_comissao = percentual_comissao / 100
valor_comissao = total_vendido * taxa_comissao
remuneracao_total = salario_fixo + valor_comissao

print("A remuneração total é: ", remuneracao_total)

