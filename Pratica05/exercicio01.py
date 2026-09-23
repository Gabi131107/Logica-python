numero = int(input("Digite um número inteiro: "))

divisao = numero // 10
resto = numero % 10
ultimo_algarismo = numero % 10

print(f"Divisão inteira por 10: {divisao}")
print(f"Resto da divisão por 10: {resto}")
print(f"Último algarismo: {ultimo_algarismo}")