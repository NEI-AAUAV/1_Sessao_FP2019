def p(x):
	return x**2 + 2*x + 3
	
def main():
	print("O valor de y para x=0 é: {}".format(p(0)))
	print("O valor de y para x=1 é: {}".format(p(1)))
	print("O valor de y para x=2 é: {}".format(p(2)))
	print("O valor de y para x=p(p(1)) é: {}".format(p(p(1))))
	
main()
