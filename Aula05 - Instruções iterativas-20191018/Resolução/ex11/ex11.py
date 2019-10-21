numero = int(input("Número? "))
soma = 0

for i in range(1, numero):
	if numero % i == 0:
		soma += i

if soma < numero:
	print("O número {} é um número deficiente.".format(numero))
if soma == numero:
	print("O número {} é um número perfeito!".format(numero))
if soma > numero:
	print("O número {} é um número abundante.".format(numero))