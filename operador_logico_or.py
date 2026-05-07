print("*** DECONTO NO CINEMA ***")

idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? (sim/não): ")

if idade >= 60 or estudante =="sim":
    print("Você ganhou desconto")
else:
    print("Você não ganhou desconto")