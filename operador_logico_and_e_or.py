print("** VERIFICANDO SE PODE COMEÇAR ACADEMIA **")

idade = int(input("Digite sua idade: "))
condicao_fisica = input("Sua condição física é boa? (sim/não): ")
atestado_medico = input("Você tem atestado médico? (sim/não): ")

if idade >= 18 and (condicao_fisica == "sim" or atestado_medico == "sim"):
    print("Você pode começar a academia")
else:
    print("Você não pode começar a academia")
