def intersects(a1, b1, a2, b2):
	boolean = True
	if b1 <= a2 or b2 <= a1:
		boolean = False
	return boolean
	
def main():
	print("Os intervalos [{},{}[ e [{},{}[ intersetam-se? {}".format(3,4,5,6,intersects(3,4,5,6)))
	print("Os intervalos [{},{}[ e [{},{}[ intersetam-se? {}".format(3,4,3,6,intersects(3,4,3,6)))

main()
