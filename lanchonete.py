print("=== BEM-VINDO À LANCHONETE DEV ===") 
nome_cliente = input("Por favor, digite o seu nome: ") 
print(f"Olá, {nome_cliente}! É um prazer atender você hoje.") 
print("----------------------------------") 

print("\n=== NOSSO CARDÁPIO ===") 
print("1. Hambúrguer Clássico - R$ 25.00") 
print("2. Refrigerante Lata - R$ 8.00") 
print("======================") 

print("\nFaça o seu pedido:") 
qtd_hamburguer = int(input("Quantos hambúrgueres você deseja? ")) 
qtd_refri = int(input("Quantos refrigerantes você deseja? ")) 

# Fazendo os cálculos 
total_hamburguer = qtd_hamburguer * 25.00 
total_refri = qtd_refri * 8.00 
valor_total = total_hamburguer + total_refri 
# Exibindo o Cupom Fiscal 
print("\n" + "="*30) 
print("          CUPOM FISCAL          ") 
print("="*30) 
print(f"Cliente: {nome_cliente}") 
print(f"Total Hambúrgueres: R$ {total_hamburguer}") 
print(f"Total Refrigerantes: R$ {total_refri}") 
print("-" * 30) 
print(f"VALOR TOTAL A PAGAR: R$ {valor_total}")
print("="*30) 
print("Obrigado pela preferência e volte sempre!") 