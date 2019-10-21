def tax(r):
	if r<= 1000:
		return 0.1*r
	elif r<=2000:
		return 0.2*r - 100
	else:
		return 0.3*r - 300
		
def main():
	print("r=1000 - resultado: {}".format(tax(1000)))
	print("r=2000 - resultado: {}".format(tax(2000)))
	print("r=2001 - resultado: {}".format(tax(2001)))
	
main()
