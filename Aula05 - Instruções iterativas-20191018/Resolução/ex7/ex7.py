# MF - Extra Food For Thought 1: O que acontece se o n for igual a 0? Como evitar?
# MF - Extra Food For Thought 2: Criar versão onde são calculadas as aproximações com n=2, n=4, n=6 e n=8 (sem serem inseridas pelo utilizador)

import math 

def leibnizPi4(n):
	aprox = 0
	for i in range(n):
		cima = (-1)**i
		baixo = 2*i+1
		aprox += cima/baixo
	return aprox

valor_referencia = math.pi/4
print("Valor de pi/4 = {:3.9f}".format(valor_referencia))
n_termos = int(input("Primeiros n termos? "))
valor_aproximado = leibnizPi4(n_termos)
print("Aproximação com primeiros {:2d} termos = {:3.9f}".format(n_termos, valor_aproximado))
print("Erro = {:3.9f}".format(valor_referencia-valor_aproximado))

# Extra Food For Thought 2 here