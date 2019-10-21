numero = int(input("Número: "))

texto = "O número indicado é "

if numero%2==0:
	texto += "par"
	
else:
	texto += "ímpar"
	
print(texto)
