#exercício 3
def max2(x, y):
	if x>=y:
		return x
	else:
		return y

#exercício 4

def max3(x,y,z):
	if max2(x,y)==max2(x,z):
		return x
	return max2(y,z)

def main():
	print("O máximo entre 3 e 5 é: {}".format(max2(3,5)))
	print("O máximo entre 3, 4 e 5 é: {}".format(max3(3,4,5)))
	
main()
