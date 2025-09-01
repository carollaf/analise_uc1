idade = int(input("Digite a idade: "))

if idade in range(5, 8):
    print("Categoria 1")
elif idade in range(8, 11):
    print("Categoria 2")
elif idade in range(11, 15):
    print("Categoria 3")
elif idade in range(15, 18):
    print("Categoria 4")
else:
    print("Sem categoria")
