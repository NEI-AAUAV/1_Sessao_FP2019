def mdc(a,b):
	if a%b==0:
		return b
	else:
		return mdc(b,a%b)
		
def main():
	print("O máximo divisor comum entre 20 e 56 é: {}".format(mdc(20,56)))
	
main()
