def Fibonacci(n):
	f0 = 0
	f1 = 1
	for i in range(n):
		temp = f0 + f1
		f0 = f1
		f1 = temp
	return f0

for i in range(10):
	print(Fibonacci(i))