print ("OBRIGADA POR ENVIAR SEU CURRÍCULO PARA EMPRESA")

idade = int(input("Digite sua idade: "))
cnh = input("Tem CNH? (sim/não): ")

if idade >= 18 and cnh == "sim":
    print("Você pode dirigir")
else: 
    print("Azedou a marmita pra você")