
combustivel = 1.4

desconto = 0.1

litros = float(input("Litros abastecidos: "))

preco = 1.4 * litros

if litros > 40:
	preco *= (1-desconto)
	
print("Custo: {} euros".format(round(preco, 2)))
