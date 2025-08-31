velocidade = int(input("Digite a velocidade: "))

if velocidade <= 80:
    print("Velocidade dentro do limite.")
else:
    multa = (velocidade - 80) * 5
    print("Você ultrapassou o limite de velocidade!")
    print(f"Multa: R$ {multa:.2f}")