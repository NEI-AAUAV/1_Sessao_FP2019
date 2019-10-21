def sequenciaReais():
	soma = 0.0
	contagem = 0
	maximo = 0
	minimo = 0
	while True:
		num = input("Numero? ")
		if num == "":
			break
		num = float(num)
		if contagem == 0:
			maximo = num
			minimo = num
		contagem += 1
		soma += num
		if maximo < num:
			maximo = num
		if minimo > num:
			minimo =  maximo
	print("{:d} números introduzidos.".format(contagem))
	print("Média = {:3.3f}".format(soma/contagem))
	print("Valor mínimo = {:3.5f}".format(maximo))
	print("Valor máximo = {:3.5f}".format(minimo))

sequenciaReais()