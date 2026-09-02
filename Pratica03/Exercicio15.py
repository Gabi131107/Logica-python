nome = input("Nome do funcionário: ")
salario = float(input("Salário: "))
bonus = float(input("Bônus: "))

total = salario + bonus

print("===== PAGAMENTO =====")
print(f"Funcionário: {nome}")
print(f"Salário: R$ {salario}")
print(f"Bônus: R$ {bonus}")
print(f"Total a receber: R$ {total}")
