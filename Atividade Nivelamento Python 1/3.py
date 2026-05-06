# Entrada das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

print(f"\nMédia: {media:.1f}")

# Questão 2: Verificação da Situação
if media >= 70:
    situacao = "Aprovado"
elif media < 40:
    situacao = "Reprovado"
else:
    situacao = "Final"

print(f"Situação: {situacao}")

# Questão 3 (DESAFIO): Atribuição de Conceito
if media >= 90:
    conceito = "A"
elif media >= 70:
    conceito = "B"
elif media >= 40:
    conceito = "C"
else:
    conceito = "D"

print(f"Conceito: {conceito}")

