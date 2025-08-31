nota = float(input("Digite uma nota entre 0 e 10: "))

if 0 <= nota <= 10:
    print(f"Nota válida! Você digitou {nota:.2f}")
else:
    print("Nota inválida! Rode o programa e tente novamente.")