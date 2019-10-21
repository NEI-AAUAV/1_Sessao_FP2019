# MF - Extra Food For Thought: Consegues tornar a função um bocadito mais rápida? 
# Nota: Só precisas de trocar exatamente 3 caracteres
# Nota2: Para notares a diferença, experimenta com números até 50000 (~5 segundos de diferença)
def isPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


print("Número \t Primo")
for i in range(1, 100):
	primo = isPrime(i)
	print("{:3d} \t {:3s}".format(i, str(primo)))