CTP = float(input("Nota CTP: "))

CP = float(input("Nota CP: "))


nota_final = CTP *0.5 + CP *0.5

if CTP < 7.5 or CP < 7.5:
	nota_final = 66

if nota_final == 66 or nota_final <= 9.5:
	print("Reprovou. Nota atual: {}".format(round(nota_final)))
	ATPR = float(input("Nota ATPR: "))
	APR = float(input("Nota APR: "))
	
	if ATPR < 7.5 or APR < 7.5:
		nota_final = 66
	else:
		nota_final = ATPR *0.5 + APR *0.5

print("A nota final é: {}".format(round(nota_final)))
