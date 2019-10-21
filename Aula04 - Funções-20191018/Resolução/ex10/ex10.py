def countdown(N):
	print(N)
	if N>1:
		countdown(N-1)
		
def main():
	print("Countdown para N=10:\n")
	countdown(10)
	
main()
