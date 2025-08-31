idade = int(input("Digite a idade: "))

if idade < 16:
    print("Ela não pode votar.")
elif idade >= 18 and idade < 70:
    print("O voto é obrigatório.")
else:
    print("O voto é opcional.")
