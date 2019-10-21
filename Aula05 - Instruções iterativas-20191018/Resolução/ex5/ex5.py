def factorial(n):
	fact = 1
	# Food for Thought: De que outra forma poderiamos 
	# Fazer a função?
	while n > 0:
		fact *= n
		n = n-1
	return fact

for i in range(1,11):
	print("Factorial de {:2d} = {:7d}".format(i, factorial(i)))